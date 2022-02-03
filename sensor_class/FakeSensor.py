import random
from BaseSensor import Base_Sensor

class Fake_Sensor(Base_Sensor):
    def __init__(self):
        # Initialize the superclass
        sensor_name = "Fake Sensor"
        super().__init__(sensor_name)

    def getReading(self):
        return random.randint(5,10)