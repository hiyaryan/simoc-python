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
        self.temperature_offset = 3.5 # Number based on comparison with SCD-30


    def getReading(self):
        temperature = (self.sensor.temperature - self.temperature_offset, "*C")
        humidity = (self.sensor.relative_humidity, "%")
        pressure = (self.sensor.pressure, "hPa")
        altitude = (self.sensor.altitude, "m")
        gas = (self.sensor.gas, "Ohms")
        return {"temperature":temperature, "humidity":humidity,
                "pressure":pressure,"altitude":altitude,"resistance":gas}

    def getBaseline(self):
        pressure_oversampling =  self.sensor.pressure_oversample
        humidity_oversampling =  self.sensor.humidity_oversample
        temperature_oversampling =  self.sensor.temperature_oversample
        filter_size = self.sensor.filter_size
        temp_offset = self.temperature_offset
        return {"pressure_oversampling":pressure_oversampling,
                "humidity_oversampling":humidity_oversampling,
                "temperature_oversampling":temperature_oversampling,
                "filter_size":filter_size,
                "temperature_offset":temp_offset }

    def setPressureSampling(self, sampling_rate_desired):
        self.sensor.pressure_oversample(sampling_rate_desired)
        
    def setHumiditySampling(self, sampling_rate_desired):
        self.sensor.humidity_oversample(sampling_rate_desired)

    def setTemperatureSampling(self, sampling_rate_desired):
        self.sensor.temperature_oversample(sampling_rate_desired)

    def setFilterSize(self,  correctedFilterSize):
        self.sensor.filter_size(correctedFilterSize)