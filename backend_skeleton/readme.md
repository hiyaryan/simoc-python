This folder contains 3 scripts that demonstrate the general communication pattern.
central.py is the stand-in for the main backend server, and sensor.py represents
multiple sensors that can connect to central.py. front.py is a terminal
console front end.

To run these scripts, use the shell script. 

- sudo chmod 777 startup.sh
- ./startup.sh

This starts central.py, then front.py which must connect first. Then as many
sensors as you want can be started. startup.sh starts 2 sensor scripts. 

Central uses asyncio to gather data from sensors, and send it to front when front
makes a request. In this version of the file, the sensors are not yet set up to
gather sensor data (although we have that in another script) but you can enter
any data into the sensor terminal, and center.py appends it to a list. When you 
type "data" in front.py it will send that list from central.py to front.py 
(and clear the list of unsent items from central.)


The Central.py script also prints input to simoc-livedata-init.json in the following format. New entries are added to "total_production" with a +1 key
{
	"sam_config": {
		"storages": {
			"air_storage":[
				{
					"id":1,
					"atmo_o2":0,
					"atmo_co2":0,
					"atmo_n2":0,
					"atmo_ch4":0,
					"atmo_h2":0,
					"atmo_h2o":0,
		 			"total_capacity":{
		 				"value":0,
		 				"unit":"kg"
		 			}
		 		}
		 	]
		 }
	},
	"parameters": {
	},
	"total_production": {
		"1":{
			"atmo_co2":{
				"value":0,
				"unit":"kg"
			}
		}
	}
}




