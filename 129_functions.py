# 129 - Using Functions in-depth (129_functions.py)
# US#80    Python Practice
# Task #129 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/129

# Meridith Greythorne
# SER401 Capstone
# Version 1.0

# This file explains and demonstrates how to use functions

# For more information on how methods and functions differ, please see 128_methods_and_function.py

# Function: A block of code which only runs when called
# Resource: https://www.w3schools.com/python/python_functions.asp

# CONTENTS
#    I. Function example (RE: Task 128)
#   II. Built-in Functions for SIMOC implementation
#  III. User-defined Functions
#   IV. Anonymous Functions
#    V. Calling a Function
#   VI. Function Arguments


# I. Function example (this just prints out the string "This is my function!"
def my_function():
    print("This is my function!")
    
my_function()

# II. BUILT-IN FUNCTIONS (reduced list)
# Here is a list of built-in functions that might come in handy for our implementation
# This is not a complete list - for all future work, please refer to the Python documentation here for all built-in functions: 
# https://docs.python.org/3/library/functions.html
# You can also see a full list of built-in functions in 128_methods_and_function.py
#
# abs(x) - Returns the absolute value of a number, x
# bool([value]) - Converts the given value to true/false. Returns False for None, False, zero value in any type (0, 0.0, etc.), empty lists, 
#     empty tuples, empty strings, empty dictionaries.
# float([value]} - Returns a float number, taken from the number/string value
# int([x]) - Returns an integer taken from the number/string x
# len(o) - Returns a number per the length of object o, where o is a sequence or collection
# max(n1, n2, n3....nm) - Returns the max value of the items provided. These are compared alphabetically, if the args are strings.
# max(iterable) - Returns the max value inside of an iterable (e.g. list, str, tuple, dict)
# min(n1, n2, n3....nm) - Returns the min value of the items provided. These are compared alphabetically, if the args are strings.
# min(iterable) - Returns the min value inside of an iterable (e.g. list, str, tuple, dict)
# next(iterator) - Returns the next item from an iterator
# round(number) - Returns number rounded to nearest integer
# round(number, ndigits) - Returns number rounded to ndigits
# str(x) - Returns x converted to string
# sum(iterable) - Returns sum of all items in the iterable (usually numbers)
# sum(iterable, start) - Returns sum of all items in the iterable + start



# III. USER-DEFINED FUNCTIONS
# Define a function using the keyword def followed by the name, parenthesis then a colon
# The body is then defined on the next indentation
def hello():
    print("Hello world!")


# Call the function directly using parenthesis and passing any required arguments
hello()

# IV. BEST PRACTICES
# When creating functions, keep it simple.
# In order to keep the functions easy-to-understand...
#    1. Keep the function small
#    2. Keep it simple (do one thing)
#    3. Use descriptive naming practices (e.g. not just 'my_func')
#    4. Comments can be useful in describing the functionality, and are recommended if not required
#    5. Minimize arguments required (many resources say that 4 is the upper end of # of arguments)
#
# Sometimes, the above can be hard. When running into an overly-complicated function, think about how it can be simplified or split up into 2 or 
# more functions instead. It is easier to understand a function when it has a simple use.


# IV. ANONYMOUS FUNCTIONS/LAMBDA FUNCTIONS
# Summary
#     Anonymous functions (AKA 'Lambda functions') are functions that are defined without a name, and are therefore not directly called. These functions...
#         1. Are not defined with keyword "def", instead using the "lambda" keyword
#         2. Do not have a body like a standard function

#     The general syntax is as follows:
#        lambda arguments: expression

# Usage
#     Use lambda functions to shorten code

# Define an anonymous function with keyword lambda and 'n' number of arguments
# lambda [arg1, arg2, ... argn]:expression

# The following is an example of a standard function:

# Normal function
def linear_expression(x):
    return (3 * x) + 2


print(linear_expression(2))


# And here is aLambda function version with the same functionality as above:
linear_expression_lambda = lambda x: (3 * x) + 2

print(linear_expression_lambda(2))

# Lambda functions are ESPECIALLY useful when you need a nameless, specific, simple function for a small amount of time. 

# Commonly, Lambda functions are used as an argument for an existing function (e.g. built-in functions). For example, here is an example using the
# built-in map() function. The map() function takes in a function and a list, and returns a map object of results from applying the function over the list.

example_list = [8,5,3,8]

result = map(lambda x: x+3, example_list)
# This could also be cast to another list by encapsulating the right side in list(__)


# V. CALLING A FUNCTION
# Calling a function is executing a previously defined function
def greet(name):
    print(f'Hello {name}.') #please note this is 'f-string' formatting. More info here: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/


# The next line is calling the defined function greet()
greet("Ryan")


# VI. FUNCTION ARGUMENTS
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
    print(f'{a} + {b} = {sum}')


addition(5, 6)


# 2. Keyword arguments
# Caller identifies arguments by argument name
def language(language_name):
    print("We are learning:", language_name)


language(language_name="Python")


# 3. Default arguments
# A function called with no arguments uses a default value if it is defined with arguments
def country(country_name="USA"):
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

