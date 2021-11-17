# This script is meant to serve as the primary script for the backend.
# It will ultimately feature 3 primary functions.
 
# The first function it serves is to gather data sent from it from multiple
# sensors. This script acts as a server to all of these sensors which connect
# to it and send it sensor data.

# The second function of this script is to send data gathered from these sensors,
# packaged as JSON, to the front-end, upon request from the front-end

# The third function of this script is to store data from the sensors to a
# database and respond to front-end requests for aged data from this database.

# This version of the script does not include all of these features. The present
# version establishes connection to a front-end and sends "data" upon request.

import socket 
import asyncio 

# Thread for each sensor
async def sense(sensor_connect, sensor_address, sensor_id, attached_sensors,
                sensor_data):
    """Serve a sensor."""
    loop = asyncio.get_event_loop()
    try:
        print(f"Sensor Thread Initialized for sensor: {sensor_id}")
        while True:
            await loop.sock_sendall(sensor_connect, 
                (bytes(f'Sensor {sensor_id}, send your data!',encoding='utf-8')))
            data = (await loop.sock_recv(sensor_connect, 1024)).decode('utf-8')
            print(f"Sensor {sensor_id} : {data}")
 
            # Inform sensor data was received
            await loop.sock_sendall(sensor_connect,
                                   (b'You sent: %s' % data.encode('utf-8')))
            # Append the sensor data
            sensor_data.append(data)
            print_data(sensor_data)
    finally:
        #Close Connection
        sensor_connect.close()
        attached_sensors.remove(sensor_id)
        print_sensors(attached_sensors)

# Thread for front
async def serve_front(front_connect, front_address, sensor_data):
    """Serve the front."""
    loop = asyncio.get_event_loop()
    try:
        print(f"Connected to front! {front_address}")
        while True:
            await loop.sock_sendall(front_connect, 
                                   (bytes('Request Data!',encoding='utf8')))
            request = (await loop.sock_recv(front_connect, 1024)).decode('utf8')
            print(f"Request from front : {request}")
            if request.lower() == 'data':
              await loop.sock_sendall(front_connect,
                                (bytes(f'Your Data: {sensor_data}', 
                                                              encoding='utf8')))
            elif request.lower() == 'quit':
                print(f"FRONT has disconnected!")
                break
            else:
                 await loop.sock_sendall(front_connect,
                                (bytes(f'Unknown Command',encoding='utf8')))
            # Clear sensor data ( We probably need to save this to database 1st)
            sensor_data.clear()
            print_data(sensor_data)

    finally:
        # Close Connection
        front_connect.close()
        # Probably more needs to be done to safely shut down the front if the 
        # Front disconnects.


#Function to print current sensors
def print_data(sensor_data):
        """Print connected sensor list."""
        print("Number of unsent data elements: ", len(sensor_data))
        print("contents: ", sensor_data)

#Function to print current sensors
def print_sensors(attached_sensors):
        """Print connected sensor list."""
        print("Number of sensors: ", len(attached_sensors))
        print("List of sensor ID: ", attached_sensors)

#Function to establish a TCP host
async def server():
        """Connect to sensors and front"""
        loop = asyncio.get_event_loop()
        attached_sensors = []
        sensor_id = 0
        sensor_data = []
        try:
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_ip, server_port = 'localhost', 17400
            host_address = (server_ip, server_port)  # param1 = IP, param2 = port
            tcp_socket.bind(host_address)
            tcp_socket.listen(1)
            tcp_socket.setblocking(False)
            # First await connection to front
            print(f"Waiting for front on {server_ip} port {server_port}")
            front_connect, front_address = await loop.sock_accept(tcp_socket)
            front_details = front_connect, front_address, sensor_data
            #Start a asyncio for a sensor sending data to the system
            loop.create_task(serve_front(*front_details))
            # Next, await connection to sensors
            while True:
                print_sensors(attached_sensors)
                print(f"Waiting for sensors on {server_ip} port {server_port}")
                #Get client
                sensor_connect, sensor_address = await loop.sock_accept(tcp_socket)
                sensor_id += 1
                sensor_details = (sensor_connect, sensor_address, sensor_id, 
                                  attached_sensors, sensor_data)
                print(f"Sensor connected from {sensor_address}!")
                #Start a asyncio for a sensor sending data to the system
                loop.create_task(sense(*sensor_details))
                attached_sensors.append(sensor_id)
        finally:
            tcp_socket.close()

if __name__ == '__main__':
    try:
        print("CENTRAL")
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(server())
        loop.run_forever()
    except Exception as exception:
        # Pass the exemption
        print(exception)
        pass
    finally:
        loop.close()
