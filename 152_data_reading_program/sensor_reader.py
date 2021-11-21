# This script is used to gather data from the SCD-30 sensor attached to
# the MCP-2221. This script is influenced by Carter Nelson and
# Bryan Siepert's scripts written for Adafruit Industries in 2020 and 2021
# It enhances these scripts by calling the linux export statement directly,
# By avoiding any kind of scd.reset() or alternative method which crashes
# the sensor, and by recovering from failure to read from the SCD-30
# by trying again next time instead of just crashing altogether.
# This script has allowed me to continuously run the sensor for over 8 hours
# as opposed to the one they provide which crashes in a few minutes
# and the alternate reset method they propose which tends to crash
# in about 30 minutes.

# @author Greg Ross, version 3, November 1,2021

# Normal Packages
import os
os.environ['BLINKA_MCP2221'] = '1'
import sys
import time
# Special packages
try:
    import busio
except RuntimeError:
    print("Script failed during busio import. Probably the sensor is not plugged in.")
    sys.exit()
    
import adafruit_scd30

if 'BLINKA_MCP2221' not in os.environ:
    print(f'Before running this program, type "export BLINKA_MCP2221=1"'
          f'in the same terminal window.')
    sys.exit()

import board # For MCP-2221

# Variables to enhance precision of sensor

# Temperature Offset - Ideally you should have a temperature sensor that is
# independent of this sensor since this sensor generates heat as it is used
# The temperature offset is the difference between ambient temperature and
# the onboard temperature sensor. T_offset = Tscd_30 - Treferefence
# set with scd.temperature_offset = OFFSET_VALUE. Every tick is 0.01*C (uint16)
# Uses last value set before repowering.

# There are also methods for calibration of the sensor but since they come calibrated
# it might not be good to change unless you have a sensor to compare it against or
# have the right environment for autocalibration (requires access to fresh air, and 5 days).


# From Carter's Script, it is recommended to start with a frequency
# of 50 Khz due to "Clock Stretching".
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

# The scd.reset() method is known to cause issues with the MCP-2221
# A script written by Adafruit offered an alternative reset method
# but it also caused issues after testing, so it is best never to
# invoke the reset method.

# Alitude, set with with scd.altitude = ALTITUDE (uint16, height above sea level in meters)
# Seting altitude is disregarded when ambient pressure is given to the system.
# Ambient Pressure, set with scd.ambient_pressure = PRESSURE_VALUE. Default
# value is 1013.25 mBar   uint16 700 to 1400 range, 0 sets to default.

# The measurement interval can be changed with this, but it still seems to take measurements
# at random time intervals just can be set "close" to this interval. The fastest interval
# combined with interpolation or just most recent reading seems like the best way to me.
# Can be increased to make a recent reading closer to another time step if we tried
# to synchronize it. Interpolation can be done either before data is saved or after
# data is retrieved from storage but prior to packaging in JSON.
# scd.measurement_interval = INTERVAL 

def get_altitude():
    if len(sys.argv) > 1:
        try:
            altitude = int(sys.argv[1])
            print(f"Altitude entered: {altitude} m")
            scd.altitude = altitude
        except ValueError:
            print("Parameter must be an int for altitude, defaulting to 1013.25 mBar")
    else:
        print("No altitude entered. Defaulting to 1013.25 mBar")

def sensor_loop():
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
            error_count += 1
            if error_count > 10:
                print("SENSOR FAILURE... killing program")
                sys.exit() # Kill the program because something bad is happening
        # New sensor data is only available once every 2 seconds by default, but here we
        # poll every 0.5 seconds by default, (or 4 times the measurement interval), to try
        # and catch every available update, even if there was a failure to reach the SCD-30.
        time.sleep(scd.measurement_interval/4)

#Start the sensor
get_altitude()
sensor_loop()
