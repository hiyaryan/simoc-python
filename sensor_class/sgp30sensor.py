import time
import board
import busio
import adafruit_sgp30

from BaseSensor import Base_Sensor


class sgp30(Base_Sensor):
	
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        self.sensor = adafruit_sgp30.Adafruit_SGP30(i2c)
        self.sensor.iaq_init()
        self.sensor.set_iaq_baseline(0x8973, 0x8AEE) # Numbers from adafruit example
        sensor_name = "SGP30#" + str(self.sensor.serial)
        sensor_id = Base_Sensor._count
        # Initialize the superclass
        super().__init__(sensor_name)


    def getBaseline(self):
        ''' Return sensor baseline values '''
        eCO2base = (self.sensor.baseline_eCO2, "ppm")
        TVOCbase = (self.sensor.baseline_TVOC, "ppb")
        return {"baseline_eCO2":eCO2base, "baseline_TVOC":TVOCbase}

    def getReading(self):
        hydrogen = (self.sensor.H2, "Raw Ticks")
        ethanol = (self.sensor.Ethanol, "Raw Ticks")
        eCO2 = (self.sensor.eCO2, "ppm")
        TVOC = (self.sensor.TVOC, "ppb")
        return {"hydrogen":hydrogen, "ethanol":ethanol,
                "eCO2":eCO2,"VolatileOrganicCompounds":TVOC}



