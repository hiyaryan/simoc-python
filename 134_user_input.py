# 134 User Input (134_user_input.py)
# US#80    Python Practice
# Task#134 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/134?

# Ian Castellanos
# SER401 Capstone
# Version 1.0

# User input allows interactivity from the end user
# there zre rules that apply to user input and parsing that will ensure type
# safety and checking if required

# these examples can be wrapped in try catch blocks complete with error handling as
# seen in 136_error_handling.py 

# As of Python 3.6 user input uses the input function
val = input("Please enter a value: ")

# in Python 2.7 user input required raw_input function
# this is for historical knowledge and will not be used 
val2 = raw_input("Please enter another value: ")

# All inputs are converted to a string regardless of how they are entered
# inputs need to be typecast to force implicit conversions
# this applies to all data types int, float, etc.
val3 = int(input("Please enter a number: "))

# multiple values can be entered from one line using split()
name, age, score = input("Enter student's name, age and score separated by space: ").split()

# a list of an unknown numbers of numbers can be taken in by using split() and map()
number_input = input("Enter a list of numbers separated by space: ").split()
print('number_input: ', number_input)

num_list = list(map(int, number_input)) 

# multiple line user input can be wrapped in a for loop
# the below function breaks when user enters blank line
student_list = []
print("Enter Student Names: ")

while True:
    name = input()
    if name:
        student_list.append(name)
    else:
        break

# user input can be checked to ensure it contains all correct types of data
string = "SIMOC"
print(string.isalpha()) # true

string2 = "SIMOC123"
print(string2.isalpha()) # false

# isnumeric() isalnum() isupper() and many more built-in functions can be used
# for additional required validation of data