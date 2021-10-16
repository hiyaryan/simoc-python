# 128 Methods and Functions (128_methods_and_functions.py)
# US#80    Python Practice
# Task#128 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/128?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates the difference between methods and functions
# Reference: https://datascienceplus.com/methods-vs-functions-in-python/

# Find more information on methods and functions below
# Methods: https://docs.python.org/3/tutorial/classes.html
# Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions


# CONTENTS
# I.    Methods
# II.   Functions
# III.  Similarities
# IV.   Differences


# I. METHODS
# A method is a function that belongs to an object
# class ClassName:
#    def method_name():
#        method_body

# Method example
class Class:
    def method(self):
        print("In the method body.")


# Use the method by referencing the object to a variable
class_reference = Class()
class_reference.method()


# II. FUNCTIONS
# A function is a block of code independent of an object
# def function_name(arg1, arg2, ...):
#    function_body

# Function example
def add(a, b):
    return a + b


print(add(50, 70))
print(add(150, 50))


# III. SIMILARITIES
# Function and
# Both functions and methods must be declared with keyword "def"


# IV. DIFFERENCES
# Functions can be called directly--independent of an object
# Methods can only be called using the class it is referenced in--dependent on an object







