# Script with common functions to reduce duplicated code.

import socket

def set_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = 'localhost'  # Change to match the docker container IP.
    server_port = 17400
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)
    return client_socket

def output_to_screen(data):
    ''' This function takes scd-30 data and prints it to the screen '''
    print(f"Time: {data['seconds']:<10.2f} "
          f"CO2: {data['co2']:>6.1f} ppm    "
          f"T: {data['temp']:<3.2f}°C    "
          f"Humidity: {data['humidity']:<3.2f}%")

