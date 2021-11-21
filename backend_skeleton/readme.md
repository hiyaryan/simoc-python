This folder contains 3 scripts that demonstrate the general communication pattern.
central.py is the stand-in for the main backend server, and sensor.py represents
 sensors that can connect to central.py. front.py is a terminal console front end.

To run these scripts, use the shell script. 

- sudo chmod 777 startup.sh
- ./startup.sh

This starts central.py, then front.py which must connect first. Then as many
sensors as you want can be started. startup.sh starts 1 sensor script for scd-30.
You must have the SCD-30 plugged in to start it. It also starts a "keyboard sensor"
simulating a second sensor.

Multiple sensors could all connect to central and central would gather all data
from all sensors to its list. 

Central uses asyncio to gather data from sensors, and send it to front when front
makes a request. In this version of the file, sensor keeps sending data to Central
as a JSON string from a live sensor. Central accumulates a list of these JSON strings.
When you just type "data" from front, you get all of the list from Central and
Central's list is cleared. In front it just prints to console the list in a messy
fashion. Some next steps: Properly format JSON for ABM, use python_data_store.py
csv saving script and incorporate into central.py these features. Also changing
communications to socketio from socket may be necessary.
