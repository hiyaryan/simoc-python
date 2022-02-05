import time
from FakeSensor import Fake_Sensor
from bme688sensor import bme688
from sgp30sensor import sgp30
from scd30sensor import scd30

myFakeSensor = Fake_Sensor()
myRealSensor = bme688()
myRealSensor2 = sgp30()
myRealSensor3 = scd30()
# BME Test
print("Sensor Name", myRealSensor.return_name())
print("Sensor ID", myRealSensor.return_id())
print("BME presents", myRealSensor.getBaseline())
for i in range(0,4):
    print(myRealSensor.getReading())
    time.sleep(1)

# SGP30 Test
print("Sensor Name", myRealSensor2.return_name())
print("Sensor ID", myRealSensor2.return_id())
print("SGP30 presets", myRealSensor2.getBaseline())
for i in range(0,4):
    print(myRealSensor2.getReading())
    time.sleep(1)

# BME Test
print("Sensor Name", myRealSensor.return_name())
print("Sensor ID", myRealSensor.return_id())
print("BME presents", myRealSensor.getBaseline())
for i in range(0,4):
    print(myRealSensor.getReading())
    time.sleep(1)
pressure = myRealSensor.getReading()["pressure"][0]
print("Pressure: ", pressure)

# SCD30 Test
print("Sensor Name", myRealSensor3.return_name())
print("Sensor ID", myRealSensor3.return_id())
#Set pressure based on other sensor's pressure
myRealSensor3.setPressure(pressure)
print("SCD30 presets", myRealSensor3.getBaseline())
for i in range(0,4):
    print(myRealSensor3.getReading())
    time.sleep(3)



# Adding 3 fake sensors
print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())
print("Sensor Preset", myFakeSensor.getBaseline())
for i in range(0,2):
    print(myFakeSensor.getReading())
    time.sleep(1)

myFakeSensor = Fake_Sensor()

print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())
print("Sensor Preset", myFakeSensor.getBaseline())

for i in range(0,2):
    print(myFakeSensor.getReading())
    time.sleep(1)


myFakeSensor = Fake_Sensor()

print("Sensor Name", myFakeSensor.return_name())
print("Sensor ID", myFakeSensor.return_id())
print("Sensor Preset", myFakeSensor.getBaseline())
for i in range(0,2):
    print(myFakeSensor.getReading())
    time.sleep(1)