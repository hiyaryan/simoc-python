Central.py serves as a server for multiple sensors running from sensor.py. It
presently saves data in batches of 24 to consecutive numbered json files in the
format needed by the front end.

Inteprolation.py has data interpolation methods for the central.py script to use
to process data.

commonio.py has a socket setting method and a screen output method. 

sensor_methods.py can be run by itself to test sensor output to the screen. 
It also contains methods used by sensor.py. Run alone it saves data to csv.

Sensor.py runs the SCD-30 sensor and connects via TCP to central.py

Move a version of central.py with test mode off as well as a copy of 
interpolation.py and commonio.py. Turning test mode off lets the docker container
know to look to the internal host network for the sensors.

Make sure commonio on the host machine has the docker container IP address in
order to function properly.

To run these scripts locally, use the shell script. 

- sudo chmod 777 startup.sh
- ./startup.sh

This starts central.py, then sensor.py 
You must have the SCD-30 plugged in to start it. 

Multiple sensors could all connect to central and central would gather all data
from all sensors to its list.



