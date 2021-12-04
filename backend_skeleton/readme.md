This folder contains 3 scripts that demonstrate the general communication pattern.
central.py is the stand-in for the main backend server, and sensor.py represents
 sensors that can connect to central.py. front.py is a terminal console front end.

Move a version of central.py with 0.0.0.0 as the ip to the docker container
as well as functions it needs like interpolation.py and commonio.py

Make sure commonio on the host machine has the docker container IP address in
order to function properly.

To run these scripts locally, use the shell script. 

- sudo chmod 777 startup.sh
- ./startup.sh

This starts central.py, then front.py which must connect first. Then as many
sensors as you want can be started. startup.sh starts 1 sensor script for scd-30.
You must have the SCD-30 plugged in to start it. 

This folder also contains a "keyboard sensor"
simulating a second sensor. Keyboard sensor in this version of the script will
generate errors if properly formed JSON is not sent.

Multiple sensors could all connect to central and central would gather all data
from all sensors to its list. 

The Central.py script now saves raw sensor data as a CSV, and interpolates
step data to the nearest 1 second for 24 seconds before generating each csv file.

This is a necessary step towards saving the JSON scripts in intervals of 24.
This version of the script has a broken JSON saving mechanism.



