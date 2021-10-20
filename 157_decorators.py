# 157 Decorator Functions (157_decorators.py)
# US#80    Python Practice
# Task#157 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/157

# Meridith Greythorne
# SER401 Capstone
# Version 1.0

# This file demonstrates Python decorator functions


# CONTENTS
#    I. Background
#   II. General Syntax


# I. BACKGROUND
# Decorators allow us to modify function/class behavior, aka "metaprogramming"
# We wrap a function in order to extend its behavior permanently
# In order to do this, we use the function we want to extend as an argument in another function, which is wrapped in the decorator


# II. GENERAL SYNTAX

# Here is the 'normal' Python function
def normal():
    print("This is the normal function.")
    
# And here is a decorator:
def decorator(func):    #takes in a function as an argument
    def inner():        
        print("I decorate the normal function!")
        normal()
        print("I have done my job.")
    return inner

# Why use an inner function?
# decorator() will return the contained function, inner(). inner() is a wrapper that 'wraps around' the function passed in as an argument, func.
# This allows us to add funtionality around an existing function. Notice above how the wrapper puts print statements BEFORE AND AFTER the original
# function. HOWEVER, at this point, nothing has been executed - decorator() simply returns the wrapper when called.

# To use the decorator:

decorated = decorator(normal)
decorated()

# The above will print out:
#    I decorate the normal function!
#    This is the normal function.
#    I have done my job.


# ADDITIONAL RESOURCES
# https://www.python.org/dev/peps/pep-0318/
# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.programiz.com/python-programming/decorator
# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together/1594484#1594484