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
# V.    Built-in Functions
# VI.   User-defined Functions
# VII.  Anonymous Functions
# VIII. Calling a Function
# IX.   Function Arguments


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


# V. BUILT-IN FUNCTIONS
# List of all 69 built-in functions
# abs()
# delattr()
# hash()
# memoryview()
# set()
# all(
# dict()
# help()
# min()
# setattr()
# any()
# dir()
# hex()
# next()
# slice()
# ascii()
# divmod()
# id()
# object()
# sorted()
# bin()
# enumerate()
# input()
# oct()
# staticmethod()
# bool()
# eval()
# int()
# open()
# str()
# breakpoint()
# exec()
# isinstance()
# ord()
# sum()
# bytearray()
# filter()
# issubclass()
# pow()
# super()
# bytes()
# float()
# iter()
# print()
# tuple()
# callable()
# format()
# len()
# property()
# type()
# chr()
# frozenset()
# list()
# range()
# vars()
# classmethod()
# getattr()
# locals()
# repr()
# zip()
# compile()
# globals()
# map()
# reversed()
# __import__()
# complex()
# hasattr()
# max()
# round()


# VI. USER-DEFINED FUNCTIONS
# Define a function using the keyword def followed by the name, parenthesis then a colon
# The body is then defined on the next indentation
def hello():
    print("Hello world!")

    # return statement is optional
    return


# Call the function directly using parenthesis and passing any required arguments
hello()


# VII. ANONYMOUS FUNCTIONS
# These functions are not defined with keyword "def"
# They do not have a body and are not directly called

# Usage
# Use lambda functions to shorten cde

# Define an anonymous function with keyword lambda and 'n' number of arguments
# lambda [arg1, arg2, ... argn]:expression

# The following is an example of the same function defined using a standard function and
# it's lambda equivalent

# Normal function
def linear_expression(x):
    return (3 * x) + 2


print(linear_expression(2))

# Lambda function with the same functionality
linear_expression_lambda = lambda x: (3 * x) + 2

print(linear_expression_lambda(2))


# VIII. CALLING A FUNCTION
# Calling a function is executing a previously defined function
def greet(name):
    print("Hello, " + name + ".")


# The next line is calling the defined function greet()
greet("Ryan")


# IX. FUNCTION ARGUMENTS
# There a 4 types of function arguments
#   1. Required arguments
#   2. Keyword arguments
#   3. Default arguments
#   4. Variable-length arguments


# 1. Required arguments
# These arguments are passed in sequential order
# On a function call, the number of arguments must match with the function definition
def addition(a, b):
    sum = a + b
    print(f"{a} + {b} =", sum)


addition(5, 6)


# 2. Keyword arguments
# Caller identifies arguments by argument name
def language(language_name):
    print("We are learning:", language_name)


language(language_name="Python")


# 3. Default arguments
# A function called with no arguments uses a default value if it is defined with arguments
def country(country_name = "USA"):
    print("Country this file is made in:", country_name)


country("Japan")
country("England")
country()


# 4. Variable-length arguments
# The number of arguments to process is more than is specified
def series(*num):
    sum = 0
    for n in num:
        sum = n + sum

    print("Sum =", sum)


series(2, 5)
series(5, 3, 5)
series(6, 2, 3, 6)

