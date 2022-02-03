import time
from abc import ABC, abstractmethod

class Base_Sensor(ABC):
    
    _count = 0;
    def __init__(self, sensor_name):
        self.name = sensor_name
        self.id = Base_Sensor._count
        Base_Sensor._count += 1;

    def return_name(self):
        return self.name

    def return_id(self):
        return self.id

    @staticmethod
    def sensor_count():
        return count

    @abstractmethod
    def getReading(self):
        "An abstract method to return all the sensor data as a dictionary"
        return NotImplemented