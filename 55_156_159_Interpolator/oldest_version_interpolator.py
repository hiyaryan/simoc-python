# This is just an example function for interpolation of data
# @author Greg Ross
import random # For generating random numbers
import threading # See https://www.geeksforgeeks.org/multithreading-python-set-1/ for threading help
import time # For time delay

# This method performs an interpolation to a time of interest
# given two data points outside of the time of interest using 
# a linear method.
def interpolateLinear(timeOfInterest, givenTime1, value1, givenTime2, value2):
  #First determine the slope of the path between the two times. 
  # This is the slope of the line known as a linear interpolant.
  # The slope of a line where the horizontal axis is time,
  # and the vertical axis is the value to interpolate, is the 
  # rate of change in the value per unit time.
  print("Table Time: ", timeOfInterest, " Expiremental Times : ","%4.2f" %givenTime1, " ", "%4.2f" %givenTime2)
  rateOfChange = (value2-value1)/(givenTime2-givenTime1)
  # Difference between the time of interest and the fistTime
  timeDifference = timeOfInterest-givenTime1
  # The interpolated data value is the early value plus the time difference multiplied
  # by the slope (change rate) 
  interpolatedValue = value1 + rateOfChange*timeDifference;
  print("given1: ","%.2f " %value1, " given2: ", "%.2f " %value2, " interpolated: ", "%.2f " % interpolatedValue)
  # The interpolated value is returned out of this function.
  return interpolatedValue;
  
  
  
# A test of this function demonstrates the veracity of the linear interpolation. The resulting value will be between the two values
# used for interpolation.

# This function generates a fake time step for a fake sensor.
def generateFakeSensorTime(lastTime): 
  acquisitionRate = 500 #Suppose the acquisition rate is about once every 5 seconds
  acquisitionVariation = random.randint(0,40) #Suppose the time has a random 400 ms variation
  #acquisitionRate = 480 # Suppose the acquisition rate is about once every 500 ms
  #acquisitionVariation = random.randint(0,40) # Suppose the time has a random 40 ms variation

  acquisitionStepTime = acquisitionRate + acquisitionVariation # Here is computed the time step
  acquisitionStepTime = acquisitionStepTime / 1000.0 # Convert to seconds from ms
  time.sleep(acquisitionStepTime) # Create wait time realistically 
  return lastTime + acquisitionStepTime #Returns the new time step which has random variation
 
# Generates a fake sensor reading. Maybe we can imagine this as the PPM of some substance being exhaled. 
def generateFakeSensorReading(lastValue):
  generationRate = 13
  generationVariation = random.randint(0,20)
  generationStep = generationRate + generationVariation
  generationStep = generationStep/100.0
  return lastValue + generationStep
  
  # Generates a fake time+value pair from previous data point
def generateFakePair(lastTime, lastValue):
    fakePair = []
    fakePair.append(generateFakeSensorTime(lastTime))
    fakePair.append(generateFakeSensorReading(lastValue))
    return fakePair

# Fake sensor is meant to be run in a thread to generate fake sensor data  
def fakeSensor(name, startTime, startVal, timeLimit, sensorData) :
  currentTime = startTime
  currentVal = startVal
  fakePair = []
  while currentTime < timeLimit :
    fakePair = fakePair[:]
    fakePair = generateFakePair(currentTime, currentVal)
    currentTime = fakePair[0]
    currentVal = fakePair[1]
    sensorData.append(fakePair)
    #print("Sensor ", name, ": ", currentTime, " s ", currentVal)
   
  
# Simulate data acquisition and interpolation  
def generateTableData():
  startTime = 0
  startVal = 20
  tableTimeStep = 1
  tableTime = 1
  timeLimit = 100
  firstPair = []
  firstPair.append(startTime)
  firstPair.append(startVal)
  tablePair = firstPair[:]
  sensorData = []
  sensorData.append(firstPair)
  tableData = []
  tableData.append(firstPair)

  #Start a thread for a sensor sending data to the system
  sensor = threading.Thread(target=fakeSensor, args=("Contaminant PPM",startTime,startVal,timeLimit, sensorData));
  sensor.start()
  while tableTime < 101 :
    
    currentTime = sensorData[-1][0]
    #print(currentTime)
    # If the current sensor reading is more than the current table time
    # Then find the most recent reading before it and interpolate with the 
    # most recent reading after it.
    if currentTime>tableTime :  
      sensor_data_copy = sensorData[:] # Make a copy of the list of sensor data right now so that new items are not added
                                       # During the processing of the list
      # Find the points just before and after the point of interest for interpolation
      dataListLength = len(sensor_data_copy)
      smallestPairWithoutGoingUnder = sensor_data_copy[dataListLength-1]
      i = 1
      
      #Get the smallest pair without going under
      while sensor_data_copy[dataListLength - i][0] > tableTime :
        smallestPairWithoutGoingUnder = sensor_data_copy[dataListLength - i]
        i = i+1
        
      #Get the largest pair without going over
      largestPairWithoutGoingOver = sensor_data_copy[dataListLength - i]
      interpVal = interpolateLinear(tableTime, largestPairWithoutGoingOver[0], largestPairWithoutGoingOver[1], smallestPairWithoutGoingUnder[0], smallestPairWithoutGoingUnder[1])
      tablePair = tablePair[:]
      tablePair[0] = tableTime
      tablePair[1] = interpVal
      tableData.append(tablePair)
      #print("Table ", tablePair[0]," s ", tablePair[1])
      tableTime += 1
    

  
  # Join the sensor thread before quitting
  sensor.join()
  
  file = open("rawData.csv", "w")
  file.write("Time,Value\n")
  for pair in sensorData :
    line = str(pair[0])+","+str(pair[1])+"\n"
    file.write(line)
  file.close()
  
  file = open("tableData.csv", "w")
  file.write("Time,Value\n")
  for pair in tableData :
    line = str(pair[0])+","+str(pair[1])+"\n"
    file.write(line)
  file.close()
  
  return

generateTableData()
