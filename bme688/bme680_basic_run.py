import time
import board
import adafruit_bme680

i2c= board.I2C()
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# Configuration Options for BME680 - I don't know why there are two variables, I haven't tested these
# sensor.sea_level_pressure = 1013.25
# sensor.seaLevelhPa = 1014.5 # Value based on local weather report for sea level pressure

# It is recommended to add an offset temperature of -5 degrees unless a better offset is known
timer = 0
while(True):
	#  Get Readings
	temperature = sensor.temperature
	humidity = sensor.relative_humidity
	pressure = sensor.pressure
	altitude = sensor.altitude
	gas = sensor.gas
	print("-------------------------")
	print("TIME: " + str(timer) )
	print("Gas Resistance: " + str(gas) + " Ohms")
	print("Temperature: "+ str(temperature) +"*C")
	print("Humidity: "+ str(humidity) + "%")
	print("Pressure: "+ str(pressure) + " hPa")
	print("Altitude: "+ str(altitude) + " m")
	print("-------------------------")
	time.sleep(1)
	timer += 1
	