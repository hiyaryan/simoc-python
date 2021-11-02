# This script is used to gather data from the SCD-30 sensor attached to
# the MCP-2221. This script will save the data accumulated to a CSV file
# for both interpolated and non-interpolated data. It saves to CSV files
# with the latest time stamp in the name continuously every time the the 
# interval is reached.
# @author Greg Ross, version 1, November 2,2021

# Normal Packages
import os
import sys
import csv
import time
# Special packages
try:
    import busio
except RuntimeError:
    print("Script failed during busio import. "
          "Probably the sensor is not plugged in.")
    sys.exit()
    
import adafruit_scd30

# export statment is required to import board
# Set the export statment command with a system call
# in case it is not already set.
# If this system call is not made, import board will fail
# This system call sometimes works on my computer but usually fails
os.system("export BLINKA_MCP2221=1")

if 'BLINKA_MCP2221' not in os.environ:
    print('Before running this program, type "export BLINKA_MCP2221=1"'
          ' in the same terminal window.')
    sys.exit()

import board # For MCP-2221

# From Carter's Script at Adafruit, it is recommended to start with a frequency
# of 50 Khz due to "Clock Stretching".
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)


# Variables to enhance precision of sensor

# Temperature Offset - Ideally you should have a temperature sensor that is
# independent of this sensor since this sensor generates heat as it is used
# The temperature offset is the difference between ambient temperature and
# the onboard temperature sensor. T_offset = Tscd_30 - Treferefence
# set with scd.temperature_offset = OFFSET_VALUE. Every tick is 0.01*C (uint16)
# Uses last value set before repowering.

# There are also methods for calibration of the sensor but since they come 
# calibrated it might not be good to change unless you have a sensor to compare
# it against or have the right environment for autocalibration (requires access
# to fresh air, and 5 days).

# The measurement interval can be changed with this, but it still seems to take 
# measurements at random time intervals just can be set "close" to this 
# interval. The fastest interval combined with interpolation or just most recent
# reading seems like the best way to me.
# Can be increased to make a recent reading closer to another time step if 
# we tried to synchronize it. Interpolation can be done either before data is 
# saved or after data is retrieved from storage but prior to packaging in JSON.
# scd.measurement_interval = INTERVAL 

# Function Definitions

# This function performs an interpolation to a time of interest
# given two data points outside of the time of interest using
# a linear method.
def interpolate_linear(time_of_interest, data_set_low, data_set_high):
    given_time2 = data_set_high['seconds']
    given_time1 = data_set_low['seconds']    
    # Difference between the time of two measurements
    time_difference = given_time2 - given_time1
    #First determine the slope of the path between the two times.
    # This is the slope of the line known as a linear interpolant.
    # The slope of a line where the horizontal axis is time,
    # and the vertical axis is the value to interpolate, is the
    # rate of change in the value per unit time.
    rate_of_change_temp = \
       (data_set_high['temp'] - data_set_low['temp']) / time_difference
    rate_of_change_humidity = \
      (data_set_high['humidity'] - data_set_low['humidity']) / time_difference
    rate_of_change_co2 = \
      (data_set_high['co2'] - data_set_low['co2']) / time_difference

    # Difference between the time of interest and the fistTime
    time_difference = time_of_interest - given_time1
    # The interpolated data value is the early value plus the time difference
    # multiplied by the slope (change rate)
    interpolated_value_temp = \
          data_set_low['temp'] + rate_of_change_temp*time_difference
    interpolated_value_humidity = \
         data_set_low['humidity'] + rate_of_change_humidity*time_difference
    interpolated_value_co2 = \
         data_set_low['co2'] + rate_of_change_co2*time_difference
    # The interpolated value is returned out of this function.
    return dict([('seconds', time_of_interest), ('co2', interpolated_value_co2),
               ('temp',interpolated_value_temp),
               ('humidity',interpolated_value_humidity)])


# Alitude, set with with scd.altitude = ALTITUDE 
# (uint16, height above sea level in meters)
# Seting altitude is disregarded when ambient pressure is given to the system.
# Ambient Pressure, set with scd.ambient_pressure = PRESSURE_VALUE. Default
# value is 1013.25 mBar   uint16 700 to 1400 range, 0 sets to default.
def get_altitude():
    if len(sys.argv) > 1:
        try:
            altitude = int(sys.argv[1])
            print(f"Altitude entered: {altitude} m")
            scd.altitude = altitude
        except ValueError:
            print("Parameter must be an int for altitude, "
                  "defaulting to 1013.25 mBar")
    else:
        print("No altitude entered. Defaulting to 1013.25 mBar")

def get_interval_data(time_elapsed):
    cO2_ppm = scd.CO2
    temperature = scd.temperature #in *C
    humidity = scd.relative_humidity
    interval_data = dict([('seconds', time_elapsed), ('co2', cO2_ppm),
                         ('temp',temperature), ('humidity',humidity)])
    return interval_data

def sensor_loop():
    WRITE_QTY = 30 # How many interpolated time steps are desired
    desired_time_step = 1 # For interpolated data, in seconds
    interpolated_time = 0
    debugLiveData = True
    debugInterpolatedData = False
    # If the sensor does not respond to 50 requests a runtime error is thrown,
    # but usually can be ignored. If it happens more than a few times over
    # the span of a few seconds, the sensor needs to be reset.
    error_count = 0
    start_time = time.time()
    sensor_data = []
    interpolated_data = []
    while True:
        current_time = time.time()
        time_elapsed = current_time - start_time
        # Check for new data, available every 2 seconds
        try:
            if scd.data_available: # If fresh data is available, get it
                error_count = 0
                interval_data = get_interval_data(time_elapsed)
                sensor_data.append(interval_data)
                if debugLiveData: # print raw data to screen to debug sensor
                    print(f"Time: {interval_data['seconds']:<10.2f} "
                          f"CO2: {interval_data['co2']:>6.1f} ppm    "
                          f"T: {interval_data['temp']:<3.2f}°C    "
                          f"Humidity: {interval_data['humidity']:<3.2f}%")
        except RuntimeError as e:
            # Occasionally sensor does not want to respond
            # Ordinarily this should be I2C read error: max entries reached
            print(e) # Print the error
            error_count += 1
            if error_count > 10:
                print("SENSOR FAILURE... killing program")
                sys.exit() # Kill the program because something bad is happening

        # Check if there is data to interpolate
        while (len(sensor_data) > 1 and
           sensor_data[-1]['seconds'] > interpolated_time + desired_time_step):
            # Get the smallest pair without going under
            for index, data_set in enumerate(reversed(sensor_data)):
                if data_set['seconds'] > interpolated_time + desired_time_step:
                    smallest_set_without_going_under = data_set
                if data_set['seconds'] < interpolated_time + desired_time_step:
                    break

            #Get the largest pair without going over
            largest_set_without_going_over = sensor_data[-(index + 1)]
            # Interpolate to find the new value
            new_time = interpolated_time + desired_time_step
            interpolated_set = interpolate_linear(
                new_time,
                # Time and values of the largest pair
                largest_set_without_going_over,
                # Time and values of the smallest pair
                smallest_set_without_going_under
            )
            interpolated_data.append(interpolated_set)
            if debugInterpolatedData: # print new data to screen to debug sensor
                print(f"Time: {interpolated_set['seconds']:<10.2f} "
                      f"CO2: {interpolated_set['co2']:>6.1f} ppm    "
                      f"T: {interpolated_set['temp']:<3.2f}°C    "
                      f"Humidity: {interpolated_set['humidity']:<3.2f}%")
            interpolated_time += desired_time_step
        
        # If more than WRITE_QTY data points have been gathered, write to file
        if len(interpolated_data) > WRITE_QTY:

            column_names = ['time', 'co2','temp','humidity']
            file_name = f"scd_data/raw/raw_data{interpolated_time}.csv"
            #Write Raw Data
            with open(file_name, 'w', newline='') as csvfile:
                csv_writer = csv.DictWriter(csvfile, sensor_data[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(sensor_data)
            # Write Interpolated Data
            file_name = f"scd_data/interpolated/interpolated_data{interpolated_time}.csv"
            with open(file_name, 'w', newline='') as csvfile:
                csv_writer = csv.DictWriter(csvfile, interpolated_data[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(interpolated_data)

            # Reset raw and interpolated data
            # Remove all the data points smaller than the interpolated time
            # Leaving the extra for the next interpolation.
            total_vals = len(sensor_data)
            i = total_vals - 1
            while i >= 0 :
                if sensor_data[i]['seconds'] < interpolated_time:
                    sensor_data.remove(sensor_data[i])
                i -= 1
            # Just like in Java, this doesn't work in Python:
            # for i, data_set in enumerate(sensor_data): # Keep some data for interpolation
            #    if ( data_set['seconds'] < interpolated_data[-2]['seconds']):
            #        sensor_data.remove(data_set) # Remove old data
            interpolated_data.clear()

        # New sensor data is only available once every 2 seconds by default,
        # but here we poll every 0.5 seconds by default, 
        # (or 4 times the measurement interval), to try and catch every
        # available update, even if there was a failure to reach the SCD-30.
        time.sleep(scd.measurement_interval/4)
       

#Start the sensor
os.system("mkdir scd_data")
os.system("mkdir scd_data/raw")
os.system("mkdir scd_data/interpolated")
get_altitude()
sensor_loop()
