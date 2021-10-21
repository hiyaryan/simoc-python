import socket # Gives us #socket.socket() and socket.sock_stream()
import threading # For multiple connections

# Thread for each client
def serve(client_connect, client_address, client_id, clients):
    try:
        print(f"Serve {client_id}")
        while True:
            client_connect.sendall(bytes('Write something!',encoding='utf8'))
            data = client_connect.recv(80)
            data = data.decode('utf-8')
            print(f"Got from {client_id} : {data}")
            if data.lower() == 'quit':
                print(f"{client_id} has left!")
                break
            else:
                client_connect.sendall(b'You sent %s' % data.encode('utf8'))
    finally:
        #Close Connection
        client_connect.close()
        clients.remove(client_id)
        print_clients(clients)

#Function to print current clients
def print_clients(clients):
        print("Number of current Connections: ", len(clients))
        print("List of clients: ", clients)

#Function to establish a TCP host
def server():
    clients = []
    client_id = 0

    while True:
        print_clients(clients)
        # I have no idea what these parameters do: AF_INET, SOCK_STREAM
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip, server_port = 'localhost', 8000
        host_address = (server_ip, server_port) #param1 = IP, param2 = port
        #The bind() function assigns the socket to the address
        tcp_socket.bind(host_address)
        # The socket must then be set to listen mode
        tcp_socket.listen(1)
        print(f"Waiting for connection on {server_ip} port {server_port}")
        #Get client
        client_connect, client_address = tcp_socket.accept()
        client_id += 1
        client_details = client_connect, client_address, client_id, clients

        print(f"Client connected from {client_address}!")
        #Start a thread for a sensor sending data to the system
        server_thread = threading.Thread(target=serve, args=(client_details))

        clients.append(client_id)
        server_thread.start()
    # End Server Function

#Start the server!
server()