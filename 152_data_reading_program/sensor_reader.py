# This script is used to gather data from the SCD-30 sensor attached to
# the MCP-2221. This script is influenced by Carter Nelson and
# Bryan Siepert's scripts written for Adafruit Industries in 2020 and 2021
# It enhances these scripts by calling the linux export statement directly,
# By presenting the data much more cleanly
# by having a discrete function to reset the SCD and calling this function
# when necessary when the SCD-30 crashes (which happens sometimes)
# and also by recovering from failure to read from the SCD-30
# by trying again next time instead of just crashing altogether.
# Unfortunately, there is still a problem where the sensor stops working
# eventually and must be unplugged from the computer and plugged back in
# again to make it work.
# @author Greg Ross, version 1, October 29,2021

# According to Carter'script, the following commented line causes
# prevents an issue with the reset on MCP-2221
# pylint: disable=protected-access

import sys # For force quit.
import os # To do the system call to set export
# Set the export statment command with a system call
# in case it is not already set.
# If this system call is not made, import board will fail
os.system("export BLINKA_MCP2221=1")
import time # For sleep function
import adafruit_scd30 # Adafruit's Library for the SCD-30
import busio # For I2C
import board # For MCP-2221

# From Carter's Script, it is recommended to start with a frequency
# of 50 Khz due to "Clock Stretching.
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

# scd.reset() apparently isn't necessary as long as the sensor is not in an
# error state to start with. scd.reset() is alternative to the
# following which is supposed to work better for MCP-2221
def reset_scd():
    #Check if this script is run on MCP-2221 (Carter's )
    if hasattr(i2c, "_i2c"):
        if hasattr(i2c._i2c, "_mcp2221"):
            # Run the MCP-2221 reset command
            i2c._i2c._mcp2221._reset()
    else: # Run the normal reset command (for Rasperry pi GPIO for instance)
        scd.reset()

def sensor_loop():
    reset_scd() # Reset any error state currently on the sensor.
    # If the sensor does not respond to 50 requests a runtime error is thrown,
    # but usually can be ignored. If it happens more than a few times over
    # the span of a few seconds, the sensor needs to be reset.
    error_count = 0
    start_time = time.time()
    while True:
        current_time = time.time()
        time_elapsed = current_time - start_time
        # Check for new data, available every 2 seconds
        try:
            if scd.data_available:
                error_count = 0
                print(f"Time: {time_elapsed:<10.2f} "
                      f"CO2: {scd.CO2:>6.1f} ppm    "
                      f"T: {scd.temperature:<3.2f}°C    "
                      f"Humidity: {scd.relative_humidity:<3.2f}%")
        except RuntimeError as e:
            # Occasionally sensor does not want to respond
            # Ordinarily this should be I2C read error: max entries reached
            print(e) # Print the error
            error_count+=1
            if(error_count>4): # Reset SCD
                print("Resetting SCD")
            # Sometimes the sensor fails altogether and it seems like physically
            # unplugging the USB and replugging is necessary. Not an acceptable
            # solution for now. I guess I need to call a system call to reset
            # USB ports to fix this maybe.
            if(error_count>50):
                print("SENSOR FAILURE... killing program")
                exit() # Kill the program because something bad is happening
        # New sensor data is only available once every 2 seconds, but here we
        # poll every 0.5 seconds to try and catch every available update,
        # even if there was a failure to reach the SCD-30.
        time.sleep(0.5)

#Start the sensor infinite loop here
sensor_loop()
