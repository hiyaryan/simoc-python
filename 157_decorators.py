# 157 Decorator Functions (157_decorators.py)
# US#80    Python Practice
# Task#157 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/157

# Meridith Greythorne
# SER401 Capstone
# Version 1.0

# This file demonstrates Python decorator functions
# PLEASE NOTE - in general, this is an interesting Python feature which has some interesting uses. It's unlikely we will use too many of these
# during our SIMOC implementation, but you never know!


# CONTENTS
#    I. Background
#   II. General Syntax and Use
#  III. Decorating Functions with Parameters
#   IV. Decorating a function multiple times
#    V. General uses
#   VI. Additional Resources


# I. BACKGROUND
# Decorators allow us to modify function/class behavior, aka "metaprogramming"
# We wrap a function in order to extend its behavior permanently
# In order to do this, we use the function we want to extend as an argument in another function, which is wrapped in the decorator


# II. GENERAL SYNTAX AND USE

# Here is the 'normal' Python function
def normal():
    print("This is the normal function.")
    
# And here is a decorator:
def example_decorator(func):    #takes in a function as an argument
    def inner():        
        print("I decorate the normal function!")
        func()
        print("I have done my job.")
    return inner

# Why use an inner function?
# decorator() will return the contained function, inner(). inner() is a wrapper that 'wraps around' the function passed in as an argument, func.
# This allows us to add funtionality around an existing function. Notice above how the wrapper puts print statements BEFORE AND AFTER the original
# function. HOWEVER, at this point, nothing has been executed - decorator() simply returns the wrapper when called.

# To use the decorator:

normal = example_decorator(normal)
normal()

# The above will print out:
#    I decorate the normal function!
#    This is the normal function.
#    I have done my job.

# Additional use - here is another 'normal' function:

@example_decorator
def another_normal_function():
    print("I'm the second normal function.")
    
# See that @decorator that? That is functionally equivalent to
    # another_normal_function = decorator(another_normal_function)
# So instead of calling
    # another_normal_function = decorator(another_normal_function)
    # another_normal_function()
# You can just call this right off the bat:

another_normal_function()

# Which will print out:
    # I decorate the normal function!
    # I'm the second normal function
    # I have done my job
    
    
# III. DECORATING FUNCTIONS WITH PARAMETERS

# In order to decorate functions that already take in parameters, we need to address this in the inner class.
# NOTE: this inner function has access to the outer local functions.

# Here is an example decorator and normal function:

# this is the decorator
def pretty_multiply(func):
    def inner(a,b):
        print("I'm going to multiply the provided integers:")
        return func(a,b)
    return inner

# normal function
@pretty_multiply
def multiply(a,b):
    print(a*b)
    
# calling the decorated function
multiply(4,5)

# Which will print:
#    I'm going to multiply the provided integers:
#    20

    
# IV. DECORATING A FUNCTION MULTIPLE TIMES
# AKA. 'CHAINING'

# You can decorate a function multiple times by 'chaining' decorators. For example:

# Here is the first decorator
def intro(func):
    def inner(normal_text):
        print("Now introducing... the normal function!\n")
        func(normal_text)
        print("\nThank you for joining us.")
    return inner
    
# Here is the second decorator
def stars(func):
    def inner(normal_text):
        print("*" * 27)
        func(normal_text)
        print("*" * 27)
    return inner

# And lastly, the normal function
@intro
@stars
def chained_normal(normal_text):
    print(normal_text)  

chained_normal("I am the normal function!")

# Which will print:
#    Now introducing... the normal function!
#
#    ***************************
#    I am the normal function!
#    ***************************
#
#    Thank you for joining us. 


# V. GENERAL USES
# Decorators are commonly used for....
#    Visuals (as above in the chaining example)
#    Timing/Synchronization (e.g. delay function completion, making asynch functions look synchronized)
#    Checking parameters, error messages, etc.
#    For any function you use that you want to temporarily add functionality to


# VI. ADDITIONAL RESOURCES
# https://www.python.org/dev/peps/pep-0318/
# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.programiz.com/python-programming/decorator
# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together/1594484#1594484