# This script will act as a front to communicate with central.


import time
import socket
import commonio

def front_client():
    client_socket = commonio.set_socket()
    print("Backend Reached Succesfuly!")
    try:
        while True:
            print("Type 'quit' to quit.")
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Central says: {data}")
            keyInput = input("Request: ")

            client_socket.sendall(keyInput.encode('utf-8'))
            front_quit = commonio.check_for_quit(keyInput)
            if front_quit:
                break
            else:
                data = client_socket.recv(1024).decode('utf-8')
                print(f"Central says: {data}")
    finally:
      client_socket.close()


if __name__ == '__main__':
    #Start the front end!
    print("FRONT")
    front_client()


