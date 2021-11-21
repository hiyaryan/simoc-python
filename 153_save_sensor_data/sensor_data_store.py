# This script is used to gather data from the SCD-30 sensor attached to
# the MCP-2221. This script will save the data accumulated to a CSV file
# for both interpolated and non-interpolated data. It saves to CSV files
# with the latest time stamp in the name continuously every time the the 
# interval is reached.
# @author Greg Ross, version 1, November 2,2021

# Normal Packages
import os
os.environ['BLINKA_MCP2221'] = '1'
import sys
import csv
import time
from pathlib import Path
# Special packages
try:
    import busio
except RuntimeError:
    print("Script failed during busio import. "
          "Probably the sensor is not plugged in.")
    sys.exit()
    
import adafruit_scd30

if 'BLINKA_MCP2221' not in os.environ:
    print('Before running this program, type "export BLINKA_MCP2221=1"'
          ' in the same terminal window.')
    sys.exit()

import board  # For MCP-2221



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

def initialize_sensor():
    """
    Initialize the sensor.
    
    Starting with a frequency of 50 kHz is recommended
    due to "Clock Stretching".
    """
    # see Carter's script at Adafruit regarding the
    # 50 kHz recommendation
    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    scd = adafruit_scd30.SCD30(i2c)
    return scd
 
def make_file_paths():
    """Create the directories to store the saved data."""
    Path("scd_data/raw").mkdir(parents=True,exist_ok=True)
    Path("scd_data/interpolated").mkdir(exist_ok=True)


def interpolate_linear(time_of_interest, data_set_low, data_set_high):
    """
    Find the CO2, temperature, and humidity values between two data points.
    
    Given two data points and a time of interest between them,
    use linear interpolation to find the values at the given time
    and returns them in a dict.
    """
    given_time2 = data_set_high['seconds']
    given_time1 = data_set_low['seconds']
    temp_high, temp_low = data_set_high['temp'], data_set_low['temp']
    humidity_high = data_set_high['humidity']
    humidity_low = data_set_low['humidity']
    co2_high, co2_low = data_set_high['co2'], data_set_low['co2']
    # Difference between the time of two measurements
    time_difference = given_time2 - given_time1
    #First determine the slope of the path between the two times.
    # This is the slope of the line known as a linear interpolant.
    # The slope of a line where the horizontal axis is time,
    # and the vertical axis is the value to interpolate, is the
    # rate of change in the value per unit time.
    change_rate_temp = (temp_high - temp_low) / time_difference
    change_rate_humidity = (humidity_high - humidity_low) / time_difference
    change_rate_c02 = (co2_high - co2_low) / time_difference

    # Difference between the time of interest and the fistTime
    time_difference = time_of_interest - given_time1
    # The interpolated data value is the early value plus the time difference
    # multiplied by the slope (change rate)
    interpolated_temp = temp_low + change_rate_temp*time_difference
    interpolated_humidity = humidity_low + change_rate_humidity*time_difference
    interpolated_co2 = co2_low + change_rate_c02*time_difference
    # The interpolated value is returned out of this function.
    return dict(seconds=time_of_interest, co2=interpolated_co2,
                temp=interpolated_temp,
                humidity=interpolated_humidity)


# Alitude, set with with scd.altitude = ALTITUDE 
# (uint16, height above sea level in meters)
# Seting altitude is disregarded when ambient pressure is given to the system.
# Ambient Pressure, set with scd.ambient_pressure = PRESSURE_VALUE. Default
# value is 1013.25 mBar   uint16 700 to 1400 range, 0 sets to default.
def get_altitude():
    ''' This function can be used to override default pressur based on altitude '''
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
    ''' This function gets the data from the sensor directly and packages it
         with the time that the sensor data was retrieved from the sensor. '''
    cO2_ppm = scd.CO2
    temperature = scd.temperature  # in *C
    rel_humidity = scd.relative_humidity
    interval_data = dict(seconds=time_elapsed, co2=cO2_ppm,
                         temp=temperature, humidity=rel_humidity)
    return interval_data

def output_to_screen(data):
    ''' This function takes scd-30 data and prints it to the screen '''
    print(f"Time: {data['seconds']:<10.2f} "
          f"CO2: {data['co2']:>6.1f} ppm    "
          f"T: {data['temp']:<3.2f}°C    "
          f"Humidity: {data['humidity']:<3.2f}%")


def sensor_loop(desired_time_step=1, debug_live_data=False,
                                     debug_interpolated_data=False):
    ''' This function loops forever, gathering data, printing it to the screen
    if debug mode is on, and saving raw data to one .csv file while saving
    data interpolated at a specific time step to another .csv file. '''
    WRITE_QTY = 30  # How many interpolated time steps are desired
    desired_time_step = 1  # For interpolated data, in seconds
    interpolated_time = 0
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
            if scd.data_available:  # If fresh data is available, get it
                error_count = 0
                interval_data = get_interval_data(time_elapsed)
                sensor_data.append(interval_data)
                if debug_live_data:  # print raw data to screen to debug sensor
                    output_to_screen(interval_data)
        except RuntimeError as e:
            # Occasionally sensor does not want to respond
            # Ordinarily this should be I2C read error: max entries reached
            print(e)  # Print the error
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
            if debug_interpolated_data:
                 # print new data to screen to debug sensor
                output_to_screen(interpolated_set)
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
            for data_set in sensor_data[:]:
                if data_set['seconds'] < interpolated_time:
                    sensor_data.remove(data_set) # Remove old data
            interpolated_data.clear()

        # New sensor data is only available once every 2 seconds by default,
        # but here we poll every 0.5 seconds by default, 
        # (or 4 times the measurement interval), to try and catch every
        # available update, even if there was a failure to reach the SCD-30.
        time.sleep(scd.measurement_interval/4)

# If called directly, start sensor loop
if __name__ == '__main__':
    # Start the sensor script here
    scd = initialize_sensor()
    make_file_paths()
    get_altitude()
    sensor_loop(debug_interpolated_data=True, debug_live_data=True)
