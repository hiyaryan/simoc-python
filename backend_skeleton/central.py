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

import csv
import json
import socket
import asyncio
import commonio
import interpolation
from pathlib import Path


def JSONize(data):
    ''' Convert array of data to proper JSON format '''
    # Files used to load structure and save logs
    save_interval = 24
    step_number = save_interval*JSONize.file_number - save_interval + 1
    # step_data.json has the correct format for 1 array entry
    json_format_file = 'step_data.json'
    # Every interval, a new file must be created
    sensor_print_file = Path('simoc_server','res',f'step_data_{JSONize.file_number}.json')
    init = False
    
    if len(data) != save_interval:
        print(f"ERROR: DATA ({len(data)} DOES NOT MATCH SAVE INTERVAL {save_interval}!")
    #DEBUG 
    print("Data in JSONize:", data)
    
    # Load the format file to save from
    with open(json_format_file, ) as file:
        sensor_json = json.load(file)

    # Append to the array a duplicate such that there are 24.
        for i in range (0,24):
            # Open base json format file
            with open(json_format_file, ) as file:
                next_json=json.load(file)
            # See if there is production or consumption of co2
            if i > 0:  # TO DO: This should look at data from the last file!
                co2_diff = data[i]["co2"] - data[i-1]["co2"]
                if co2_diff > 0:
                    co2_production = co2_diff
                    co2_consumption = 0
                else:
                    co2_production = 0
                    co2_consumption = -co2_diff
            else:
                co2_production = 0
                co2_consumption = 0                    
            this_step = i+step_number
            # Set the value for humidity and co2
            next_json[0]["step_num"]=this_step
            next_json[0]["storage_capacities"]["air_storage"]["1"]["atmo_co2"]["value"]=data[i]["co2"]
            next_json[0]["storage_capacities"]["air_storage"]["1"]["atmo_h2o"]["value"]=data[i]['humidity']
            next_json[0]["total_production"]["atmo_co2"]["value"]=co2_production
            next_json[0]["total_consumption"]["atmo_co2"]["value"]=co2_consumption

            sensor_json.append(next_json[0])

    # Eliminate the first entry in the list which was the file that was loaded
    sensor_json.pop(0);
    with open(sensor_print_file, 'w') as file:
        file.seek(0)
        json.dump(sensor_json, file)
    
    JSONize.file_number += 1 # Increment the function satic variable
    return sensor_json
JSONize.file_number = 1 # initialize the function static variable

# Thread for each sensor
async def sense(sensor_connect, sensor_address, sensor_id, attached_sensors,
                sensor_data):

    """Serve a sensor."""
    loop = asyncio.get_event_loop()
    try:
        print(f"Sensor Thread Initialized for sensor: {sensor_id}")
        while True:
            await loop.sock_sendall(sensor_connect, 
                                    b'Sensor %d, send your data!' % sensor_id)
            data = (await loop.sock_recv(sensor_connect, 1024)).decode('utf8')

            # print(f"Sensor Original {sensor_id} : {data}")

            if data.lower() == 'quit':
                print(f"{sensor_id} has left!")
                break
            else:

                # Inform sensor data was received
                await loop.sock_sendall(sensor_connect,
                                        b'You sent: %s' % data.encode('utf-8'))
                # print("RAW DATA", data)
                # Pull the JSON out of the sent package
                JSON_split = json.loads(data)
                # Append data to end of the JSON save File
                # To do: Make it so that this JSON_appendium sends to front
                #JSON_APPENDIUM = JSONize(JSON_split["co2"])
                #To do: PACKAGE TEMP, HUMIDITY, ETC. ALSO
                # Append the sensor data
                sensor_data.append(JSON_split)
                # print_data(sensor_data)
                await asyncio.sleep(0.5)

    finally:
        # Close Connection
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
            await loop.sock_sendall(front_connect, b'Request Data!')
            request = (await loop.sock_recv(front_connect, 1024)).decode('utf8')
            print(f"Request from front : {request}")
            if request.lower() == 'data':
              await loop.sock_sendall(front_connect,
                                     f'Your Data: {sensor_data}'.encode('utf8'))

            elif request.lower() == 'quit':
                print(f"FRONT has disconnected!")
                break
            else:
                 await loop.sock_sendall(front_connect, b'Unknown Command')

            # Clear sensor data ( We probably need to save this to database 1st)
            sensor_data.clear()
            print_data(sensor_data)

    finally:
        # Close Connection
        front_connect.close()
        # Probably more needs to be done to safely shut down the front if the 
        # Front disconnects.


# Function to print current sensors
def print_data(sensor_data):
    """Print connected sensor list."""
    print("Number of unsent data elements:", len(sensor_data))
    print("contents:", sensor_data)

# Function to print current sensors
def print_sensors(attached_sensors):
    """Print connected sensor list."""

    print("Number of sensors:", len(attached_sensors))
    print("List of sensor ID:", attached_sensors)

# Function to write raw data to a CSV for long term storage
def write_raw_data_csv(sensor_data, interpolated_time):
    column_names = ['time', 'co2','temp','humidity']
    file = Path('raw_sensor_data',f'raw_data{interpolated_time}.csv')
    #Write Raw Data to CSV for storage
    with file.open('w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, sensor_data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(sensor_data)

async def process_data(attached_sensors, sensor_data):
    loop = asyncio.get_event_loop()
    WRITE_QTY = 24  # How many interpolated time steps are desired
    desired_time_step = 1  # For interpolated data, in seconds
    interpolated_time = 0
    interpolated_data = []
    debug_interpolated_data = True
    # Wait until there is data to process
    while len(sensor_data) < 1:
        await asyncio.sleep(1);

    while True:
        # Check if there is data to interpolate
        sensor_data_copy = sensor_data[:]
        while (len(sensor_data) > 1 and
           sensor_data_copy[-1]['seconds'] > interpolated_time + desired_time_step):
            # Get the smallest pair without going under
            for index, data_set in enumerate(reversed(sensor_data_copy)):
                if data_set['seconds'] > interpolated_time + desired_time_step:
                    smallest_set_without_going_under = data_set
                if data_set['seconds'] < interpolated_time + desired_time_step:
                    break

            #Get the largest pair without going over
            largest_set_without_going_over = sensor_data_copy[-(index + 1)]
            # Interpolate to find the new value
            new_time = interpolated_time + desired_time_step
            interpolated_set = interpolation.linear(
                new_time,
                # Time and values of the largest pair
                largest_set_without_going_over,
                # Time and values of the smallest pair
                smallest_set_without_going_under
            )
            interpolated_data.append(interpolated_set)
            if debug_interpolated_data:
                 # print new data to screen to debug sensor
                commonio.output_to_screen(interpolated_set)
            interpolated_time += desired_time_step
        
        # If more than WRITE_QTY data points have been gathered, write to file
        if len(interpolated_data) > WRITE_QTY:
            write_raw_data_csv(sensor_data_copy, interpolated_time)
            
            # Write Interpolated Data to JSON
            JSONize(interpolated_data[0:24])

            # Reset raw and interpolated data
            # Remove all the data points smaller than the interpolated time
            # Leaving the extra for the next interpolation.
            for data_set in sensor_data_copy:
                if data_set['seconds'] < interpolated_time:
                    sensor_data.remove(data_set) # Remove old data
            for i in range (0,24):
                interpolated_data.pop(0)

        await asyncio.sleep(1);
        print("Waiting for data...", len(sensor_data))
# Function to establish a TCP host
async def server():
    """Connect to sensors and front"""
    loop = asyncio.get_event_loop()
    attached_sensors = []
    sensor_id = 0
    sensor_data = []
    test_mode = True;
    process_details = (attached_sensors, sensor_data)
    # Start an asyncio for a sensor data processing function
    loop.create_task(process_data(*process_details))

    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # USE 0.0.0.0 for server_ip if in docker container, localhost for testing
        if test_mode:  
            server_ip, server_port = 'localhost', 17400
            print ("TEST MODE ENABLED, DISABLE FOR DOCKER CONTAINER!")
        else:
            server_ip, server_port = '0.0.0.0', 17400
        
                
        host_address = (server_ip, server_port)
        tcp_socket.bind(host_address)
        tcp_socket.listen(1)
        tcp_socket.setblocking(False)
        # First await connection to front
        print(f"Waiting for front on {server_ip} port {server_port}")
        front_connect, front_address = await loop.sock_accept(tcp_socket)
        front_details = front_connect, front_address, sensor_data



        # Start a asyncio for a sensor sending data to the system
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
        Path("raw_sensor_data").mkdir(parents=True,exist_ok=True)
        Path("simoc_server","res").mkdir(parents=True,exist_ok=True)
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(server())
        loop.run_forever()
    except Exception as exception:
        # Pass the exemption
        print(exception)
    finally:
        loop.close()
