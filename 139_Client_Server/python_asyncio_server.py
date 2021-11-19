import socket 
import asyncio 

# Thread for each client
async def serve(client_connect, client_address, client_id, clients):
    """Serve a client."""
    loop = asyncio.get_event_loop()
    try:
        print(f"Serve {client_id}")
        while True:
            await loop.sock_sendall(client_connect,b'Write something!')
            data = (await loop.sock_recv(client_connect, 80)).decode('utf8')
            print(f"Got from {client_id} : {data}")
            if data.lower() == 'quit':
                print(f"{client_id} has left!")
                break
            else:
                await loop.sock_sendall(client_connect,
                                        b'You sent %s' % data.encode('utf8'))
    finally:
        #Close Connection
        client_connect.close()
        clients.remove(client_id)
        print_clients(clients)

#Function to print current clients
def print_clients(clients):
    """Print client list and number of connections."""
    print("Number of current Connections:", len(clients))
    print("List of clients:", clients)

#Function to establish a TCP host
async def server():
        """Accept many clients forever."""
        loop = asyncio.get_event_loop()
        clients = []
        clientLoops = []
        client_id = 0
        try:
            # I have no idea what these parameters do: AF_INET, SOCK_STREAM
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_ip, server_port = 'localhost', 13000
            host_address = (server_ip, server_port) #param1 = IP, param2 = port
            #The bind() function assigns the socket to the address
            tcp_socket.bind(host_address)
            # The socket must then be set to listen mode
            tcp_socket.listen(1)
            tcp_socket.setblocking(False)
            while True:
                print_clients(clients)
                print(f"Waiting for connection on {server_ip} port {server_port}")
                #Get client
                client_connect, client_address = await loop.sock_accept(tcp_socket)
                client_id += 1
                client_details = client_connect, client_address, client_id, clients
                print(f"Client connected from {client_address}!")
                #Start a asyncio for a sensor sending data to the system
                loop.create_task(serve(*client_details))
                clients.append(client_id)
        finally:
            tcp_socket.close()

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(server())
        loop.run_forever()
    except Exception as exception:
        # Pass the exemption
        print(exception)
    finally:
        loop.close()
