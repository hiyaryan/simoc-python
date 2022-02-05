This directory is to build a sensor class for other sensors to inherit from, and to develop better understanding of class/object relations in Python such that sensors can inherit from the sensor class established by OverTheSun, and to provide better input in how to construct that class.

BaseSensor.py contains an abstract class called Base_Sensor
FakeSensor.py contains a class called Fake_Sensor that inherits from Base_Sensor
bme688sensor.py contains a class called bme688 that inherits from Base_Sensor (and works on Raspberry Pi!)
sgp30sensor.py contains a class called sgp30 that inherits from Base_SEnsor (and works on Raspberry Pi!)

TestScript instantiates the bme688, sgp30, and some fake sensors to test the functionality.

