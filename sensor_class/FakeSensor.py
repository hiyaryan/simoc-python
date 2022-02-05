import random
from BaseSensor import Base_Sensor

class Fake_Sensor(Base_Sensor):
    def __init__(self):
        # Initialize the superclass
        sensor_name = "Fake Sensor"
        super().__init__(sensor_name)

    def getReading(self):
        readingType1 = (random.randint(5,10), "unitsA")
        readingType2 = (random.randint(5,10), "unitsB")
        readingType3 = (random.randint(5,10), "unitsC")
        return {"readingType1":readingType1,"readingType2":readingType2,"readingType3":readingType3}

    def getBaseline(self):
        return "Default settings"