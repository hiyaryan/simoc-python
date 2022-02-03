import time
from FakeSensor import Fake_Sensor
from bme688sensor import bme688

myFakeSensor = Fake_Sensor()
myRealSensor = bme688()
print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())
for i in range(0,8):
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