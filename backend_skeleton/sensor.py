# This script will act as a sensor to connect to central

import sys
import time
import json
import socket
import commonio
import sensor_methods


def sensor_client(scd):
    """Run sensor client to send data from this sensor to central"""
    client_socket = commonio.set_socket()
    start_time = time.time()
    error_count = 0
    print("Connection to Central succesful!")
    try:
        while True:
            success = True
            current_time = time.time()
            time_elapsed = current_time - start_time
            print("Getting Central's message...")
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Central says: {data}")
            response = "No Data Recorded"
            # Get some sensor message to send
            updated = False
            while not updated:
                try:
                    time.sleep(scd.measurement_interval/4)
                    if scd.data_available:  # If fresh data is available, get it
                        error_count = 0
                        response = sensor_methods.get_interval_data(scd,time_elapsed)
                        response = json.dumps(response)
                        updated = True
                except RuntimeError as e:
                    print(e)
                    error_count += 1
                    updated = False
                    if error_count > 10:
                        print("SENSOR FAILURE... killing program")
                        sys.exit() # Kill the program because something bad is happening
            response = response.encode('utf-8')
            client_socket.sendall(response)
            data = client_socket.recv(1600).decode('utf-8')
            print(f"Central replies: {data}")
    finally:
      client_socket.close()

if __name__ == '__main__':
    #Start the client!
    print("SENSOR")
    scd = sensor_methods.initialize_sensor()
    sensor_methods.get_altitude(scd)
    sensor_client(scd)

