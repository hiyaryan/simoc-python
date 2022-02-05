import time
import board
import busio
import adafruit_scd30

from BaseSensor import Base_Sensor


class scd30(Base_Sensor):
	
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
        self.sensor = adafruit_scd30.SCD30(i2c)
        sensor_name = "SCD-30"
        sensor_id = Base_Sensor._count
        # Initialize the superclass
        super().__init__(sensor_name)


    def setPressure(self, pressure):
        """Set Pressure in mBar (int)"""
        self.sensor.ambient_pressure = pressure

    def setAltitude(self, altitude):
        """Set Altitude in meters"""
        self.sensor.altitude = altitude

    # Temperature Offset - Ideally you should have a temperature sensor that is
    # independent of this sensor since this sensor generates heat as it is used
    # The temperature offset is the difference between ambient temperature and
    # the onboard temperature sensor. T_offset = Tscd_30 - Treferefence
    # set with scd.temperature_offset = OFFSET_VALUE. Every tick is 0.01*C (uint16)
    # Uses last value set before repowering.
    def setTemperatureOffset(self, hundredthsOfDegrees):
        """Set Temperature Offset in hundredths of degree celsius. T offset = Tscd30 - Tref"""
        self.sensor.temperature_offset = hundredthsOfDegrees

    def setMeasurementInterval(self,interval):
        """ Set the measurement interval to hardware delay how often readings are made.
            The fastest interval of 2 has a new reading every 2.5 seconds or so """
        self.sensor.measurement_interval = interval

    def getBaseline(self):
        ''' Return sensor baseline values '''
        altitude = (self.sensor.altitude, "m")
        pressure = (self.sensor.ambient_pressure, "mBar")
        tempOffset = (self.sensor.temperature_offset, "hundredths of *C")
        measurementInterval = (self.sensor.measurement_interval, "s")
        return {"altitude":altitude, "pressure":pressure,"tempOffset":tempOffset,
                "measurementInterval":measurementInterval}

    def is_data_available():
        return self.sensor.data_available        

    def getReading(self):
        """ Get reading --- should check if ready before using """
        cO2 = (self.sensor.CO2, "ppm")
        temperature = (self.sensor.temperature, "*C")
        humidity = (self.sensor.relative_humidity, "%")
        return {"cO2":cO2, "temperature":temperature,
                "humidity":humidity}



