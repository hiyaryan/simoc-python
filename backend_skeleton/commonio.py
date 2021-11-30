# Script with common functions to reduce duplicated code.

import socket

def check_for_quit(keyInput):
    if keyInput.lower() == 'quit':
        for n in range(5, 0,-1):
            print(f"Quitting in {n} seconds");
            time.sleep(1)
        return True
    return False

def set_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '172.18.0.4'
    server_port = 17400
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)
    return client_socket
