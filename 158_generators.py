# 158 Generators (158_generators.py)
# US#80    Python Practice
# Task#158 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/158

# Meridith Greythorne
# SER401 Capstone
# Version 1.0

# This file explains and demonstrates generators in Python


# CONTENTS
#    I. Background
#   II. Generator Functions
#  III. Generator Objects
#   IV. Uses
#    V. Resources


# I. BACKGROUND
# IF A DEF BLOCK CONTAINS A 'yield', THE FUNCTION IS AUTOMATICALLY CONSIDERED A GENERATOR FUNCTION
# This is because Generators generate values and uses 'yield' to do so, rather than 'return'. Generators make iterations easy, 
# as you don't have to spend time implementing a specific iterator class, or keep track of states and timeout.
# In it's primary use, a genorator will return an iterator object which we can iterate over easily.


# II. GENERATOR FUNCTIONS
# Defined like a normal function but uses 'yield' instead of 'return'
# Returns an object that is iterable

# Here is a simple example of a generator FUNCTION:
def example_generator():
    yield 1
    yield 2
    yield 3
    
# These 'yields' are interesting, because once a yield is reach, the function is paused. You have control over the calls.
# Here is how we can use the iterator:

for val in example_generator(): #We can iterate over the generator as it is iterable
    print(val)

# Which will print:
# 1
# 2
# 3


# III. GENERATOR OBJECTS
# Rather than acting as a standard function as above, generator objects return iterable objects. This is especially useful if you want to use next() to step through the
# generator incrementally. Here is an examply that's pretty similar to the above:

def example_generator_object():
    print("This will print first, then stop")
    yield 1
    
    print("This will print second, then stop")
    yield 2
    
    print("This will print third, then stop")
    yield 3 

# And here is how we can access a value:

gen = example_generator_object()
print(next(gen))

# Which will print...
#    This will print first, then stop
#    1

# See how the print stops at the first yield? When using and calling generators this way, you have control over which blocks are called when, based on yields.
# Here is the continuation...

print(next(gen))
print(next(gen))
#    This will print second, then stop
#    2
#    This will print third, then stop
#    3


# IV. USES
# Generators are a useful way to avoid implementing iterators. For example, reading large files, data processing, etc. For example, here is a generator example for calculating
# fibibacci numbers, found here: https://stackoverflow.com/questions/3953749/python-fibonacci-generator

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
        
# Called via:
print(list(fib(1))) # where 1 is replaced with the number of fibonacci numbers to print


# V. ADDITIONAL RESOURCES
# https://wiki.python.org/moin/Generators
# https://www.programiz.com/python-programming/generator
# https://www.geeksforgeeks.org/generators-in-python/