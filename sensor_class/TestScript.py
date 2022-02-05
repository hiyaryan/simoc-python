import time
from FakeSensor import Fake_Sensor
from bme688sensor import bme688
from sgp30sensor import sgp30

myFakeSensor = Fake_Sensor()
myRealSensor = bme688()
# BME Test
print("Sensor Name", myRealSensor.return_name())
print("Sensor ID", myRealSensor.return_id())
for i in range(0,4):
    print(myRealSensor.getReading())
    time.sleep(1)

# SGP30 Test
myRealSensor2 = sgp30()
print("Sensor Name", myRealSensor2.return_name())
print("Sensor ID", myRealSensor2.return_id())
print("SGP30 presets", myRealSensor2.getBaseline())
for i in range(0,4):
    print(myRealSensor2.getReading())
    time.sleep(1)

# BME Test
print("Sensor Name", myRealSensor.return_name())
print("Sensor ID", myRealSensor.return_id())
for i in range(0,4):
    print(myRealSensor.getReading())
    time.sleep(1)



# Adding 3 fake sensors
print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())

for i in range(0,2):
    print(myFakeSensor.getReading())
    time.sleep(1)

myFakeSensor = Fake_Sensor()

print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())

for i in range(0,2):
    print(myFakeSensor.getReading())
    time.sleep(1)


myFakeSensor = Fake_Sensor()

print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())

for i in range(0,2):
    print(myFakeSensor.getReading())
    time.sleep(1)