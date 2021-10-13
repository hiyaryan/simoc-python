# This is just an example function for interpolation of data
# it is tested with a fake sensor and some other functions
# for creating fake sensor data.
# @author Greg Ross
import random # For generating random numbers
# For threading help see:
# https://www.geeksforgeeks.org/multithreading-python-set-1/ 
import threading 
import time # For time delay
import csv

# This method performs an interpolation to a time of interest
# given two data points outside of the time of interest using 
# a linear method.
def interpolate_linear(time_of_interest, given_time1, value1, \
                                         given_time2, value2):
  #First determine the slope of the path between the two times. 
  # This is the slope of the line known as a linear interpolant.
  # The slope of a line where the horizontal axis is time,
  # and the vertical axis is the value to interpolate, is the 
  # rate of change in the value per unit time.
  rate_of_change = (value2-value1) / (given_time2-given_time1)
  # Difference between the time of interest and the fistTime
  time_difference = time_of_interest-given_time1
  # The interpolated data value is the early value plus the time difference 
  # multiplied by the slope (change rate) 
  interpolated_value = value1 + rate_of_change * time_difference;
  # Print interpolated point to screen
  print("[", time_of_interest, "s ", "%.2f" % interpolated_value, \
   "K]. Interpolated from:  [", "%4.2f" %given_time1, "s ", \
   "%.2f " %value1, "K] and [", "%4.2f" %given_time2, "s ", "%.2f" %value2, \
   "K]")
  # The interpolated value is returned out of this function.
  return interpolated_value;
  
# This function generates a fake time step for a fake sensor.
def generate_fake_sensor_time(last_time): 
  #Suppose the acquisition rate is about once every 0.5 seconds
  acquisition_rate = 500 
  #Suppose the time has a random 40 ms variation
  acquisition_variation = random.randint(0, 40) 
  # Here is computed the time step
  acquisition_step_time = acquisition_rate + acquisition_variation 
  # Convert to seconds from ms
  acquisition_step_time = acquisition_step_time / 1000
  time.sleep(acquisition_step_time) # Create wait time realistically 
  #Returns the new time step which has random variation
  return last_time + acquisition_step_time 
 
# Generates a fake sensor reading. 
# Maybe we can imagine this as the PPM of some substance being exhaled. 
def generate_fake_sensor_reading(last_value):
  generation_rate = 13
  generation_variation = random.randint(0, 20)
  generation_step = generation_rate + generation_variation
  generation_step = generation_step / 100
  return last_value + generation_step
  
# Generates a fake time+value pair from previous data point
def generate_fake_pair(last_time, last_value):
    fake_pair = []
    fake_pair.append(generate_fake_sensor_time(last_time))
    fake_pair.append(generate_fake_sensor_reading(last_value))
    return fake_pair

# Fake sensor is meant to be run in a thread to generate fake sensor data  
def fake_sensor(name, start_time, start_value, time_limit, sensor_data) :
  current_time = start_time
  current_value = start_value
  fake_pair = []
  while current_time < time_limit :
    fake_pair = fake_pair[:]
    fake_pair = generate_fake_pair(current_time, current_value)
    current_time = fake_pair[0]
    current_value = fake_pair[1]
    sensor_data.append(fake_pair)
  
# Function to simulate data acquisition and interpolation  
def generate_table_data():
  start_time = 0
  start_value = 20
  table_time_step = 1
  table_time = 1
  time_limit = 100
  first_pair = []
  first_pair.append(start_time)
  first_pair.append(start_value)
  table_pair = first_pair[:]
  sensor_data = []
  sensor_data.append(first_pair)
  table_data = []
  table_data.append(first_pair)

  #Start a thread for a sensor sending data to the system
  sensor = threading.Thread(target=fake_sensor, \
     args=("Contaminant PPM",start_time,start_value,time_limit, sensor_data));
  sensor.start()
  
  while table_time < 101 :
    current_time = sensor_data[-1][0]
    #print(current_time)
    # If the current sensor reading is more than the current table time
    # Then find the most recent reading before it and interpolate with the 
    # most recent reading after it.
    if current_time > table_time :  
      sensor_data_copy = sensor_data[:] # Make a copy of the list of sensor
                                        # data right now so that new items 
                                        # are not added During the processing 
                                        # of the list
      # Find the points just before and after the 
      # point of interest for interpolation
      data_list_length = len(sensor_data_copy)
      smallest_pair_without_going_under = sensor_data_copy[data_list_length - 1]
      i = 1
      
      #Get the smallest pair without going under
      while sensor_data_copy[data_list_length - i][0] > table_time :
        smallest_pair_without_going_under = \
                               sensor_data_copy[data_list_length - i]
        i = i + 1
        
      #Get the largest pair without going over
      largest_pair_without_going_over = sensor_data_copy[data_list_length - i]
      interpolated_value = interpolate_linear(table_time, \
      largest_pair_without_going_over[0], largest_pair_without_going_over[1], \
      smallest_pair_without_going_under[0], \
      smallest_pair_without_going_under[1])
      table_pair = table_pair[:]
      table_pair[0] = table_time
      table_pair[1] = interpolated_value
      table_data.append(table_pair)
      table_time += 1
      
  # Join the sensor thread before quitting
  sensor.join()
  
  #Write Raw Data
  with open('raw_data.csv', 'w', newline='') as csvfile:
    column_names = ['time', 'value']
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(column_names)   
    csv_writer.writerows(sensor_data)
  # Write Interpolated Data
  with open('talbe_data.csv', 'w', newline='') as csvfile:
    column_names = ['time', 'value']
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(column_names) 
    csv_writer.writerows(table_data)
  
  
#Actually run the simulation
generate_table_data()
