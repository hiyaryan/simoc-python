import time
import board
import adafruit_bme680
import random
from BaseSensor import Base_Sensor


class bme688(Base_Sensor):
	
    def __init__(self):
        # Initialize the superclass
        sensor_name = "BME688"
        sensor_id = Base_Sensor._count
        super().__init__(sensor_name)
        i2c= board.I2C()
        self.sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)


    def getReading(self):
        temperature = (self.sensor.temperature, "*C")
        humidity = (self.sensor.relative_humidity, "%")
        pressure = (self.sensor.pressure, "hPa")
        altitude = (self.sensor.altitude, "m")
        gas = (self.sensor.gas, "Ohms")
        return {"temperature":temperature, "humidity":humidity,
                "pressure":pressure,"altitude":altitude,"resistance":gas}

    def getBaseline(self):
        return "Default Settings"

