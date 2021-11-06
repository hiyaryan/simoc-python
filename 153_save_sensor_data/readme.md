This is a script that combines sensor reading with interpolation.
It generates subdirectories for raw and interpolated sensor data. 
The next step after this script is to write another script that can take
sensor data, either from CSV or direct from the sensors, and JSONize it.
From there, it will just need to be sent to the front end.

When you run this script, if you specifiy an integer after running it, such as
python3 sensor_data_store.py 5300 it will alter the pressure level that of 5300 
meters on Earth instead of defaulting to 1013.25 mBar.

This script is now functionalized so that these functions, in a final version
of this script, could be invoked from another script. For example, the sensor
loop will take a parameter for desired time step and whether to print to the 
screen.

For example:
-sensor_loop(desired_time_step=10) will set 10 seconds to be the time step data interpolates to.
-sensor_loop(debugInterpolatedData=True) will print interpolated data during data collection
-sensor_loop(debugLiveData=True) will print the raw data during data collection
-initialize_sensor() will return the scd so you can pull results from it

This script attempt to invoke the command "export BLINKA_MCP2221=1" but may fail
which will require you to manually enter this command prior to running the script.
It will let you know if it didn't work. It usually doesn't work, for unknown reasons.

csv files have the current format:

seconds,co2,temp,humidity
