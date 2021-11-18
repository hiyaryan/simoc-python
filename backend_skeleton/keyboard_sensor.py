# This script will act as a sensor to connect to central

import time
import socket
import commonio

def keyboard_client():
    client_socket = commonio.set_socket()
    print("Connection succesful!")
    try:
        while True:
            print("Type 'quit' to quit.")
            data = client_socket.recv(80)
            print(f"Server says: {data.decode('utf-8')}")
            keyInput = input("Response: ")

            client_socket.sendall(keyInput.encode('utf-8'))
            client_wants_to_quit = commonio.check_for_quit(keyInput)
            if(client_wants_to_quit):
                break
            else:
                data = client_socket.recv(80)
                print(f"Server says: {data.decode('utf-8')}")
    finally:
      client_socket.close()

#Start the fake sensor keyboard client!
print("SENSOR (KEYBOARD)")
keyboard_client()
