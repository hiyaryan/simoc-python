import socket
import time

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = 'localhost'
    server_port = 13000
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)
    print("Connection succesful!")
    try:
        while True:
            print("Type 'quit' to quit.")
            data = client_socket.recv(80)
            print(f"Server says: {data.decode('utf-8')}")
            keyInput = input("Response: ")

            client_socket.sendall(keyInput.encode('utf-8'))
            if keyInput.lower() == 'quit':
                for n in range(5,0,-1):
                    print(f"Quitting in {n} seconds");
                    time.sleep(1)
                break
            else:
                data = client_socket.recv(80)
                print(f"Server says: {data.decode('utf-8')}")
    finally:
      client_socket.close()

#Start the client!
client()
