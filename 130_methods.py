# 130 Methods (130_methods.py)
# US#80    Python Practice
# Task#130 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/130

# Meridith Greythorne
# SER401 Capstone
# Version 1.0

# This file explains and demonstrates methods in Python in-depth


# CONTENTS
#    I. Background
#   II. Methods (per 128_methods_and_functions.py)
#  III. Magic Methods
#   IV. Using Magic Methods to Override
#    V. Additional resources


# I. BACKGROUND
# Methods in Python are like functions, however they must be called using an object, and are therefore created within a class.


# II. METHODS (per 128_methods_and_functions.py)
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


# III. MAGIC METHODS
# Magic methods in Python (AKA 'dunders'), are methods used to add functionality which can't be implemented as a normal method. These methods
# are not meant to be called directly by the programmer, however they shed some light on internal workings like built-in functions and classes.

# Dunder methods are identified using TWO underscores (_) at the beginning and end of its name. For example:
#    __add__()    Which gets called automatically when two numbers are added using the '+' operator

# Here are some example Magic Methods:
#__abs__,__add__,__and__,__bool__,__ceil__,__class__,__delattr__,__dir__,__divmod__,__doc__,__eq__,__float__,__floor__,__floordiv__,__format__,
#__ge__,__getattribute__,__getnewargs__,__gt__,__hash__,__index__,__init__,__init_subclass__,__int__,__invert__,__le__,__lshift__,__lt__,__mod__,
#__mul__,__ne__,__neg__,__new__,__or__,__pos__,__pow__,__radd__,__rand__,__rdivmod__,__reduce__,__reduce_ex__,__repr__,__rfloordiv__,__rlshift__,
#__rmod__,__rmul__,__ror__,__round__,__rpow__,__rrshift__,__rshift__,__rsub__,__rtruediv__,__rxor__,__setattr__,__sizeof__,__str__,__sub__,__subclasshook__,
#__truediv__,__trunc__,__xor__


# IV. USING MAGIC METHODS TO OVERRIDE
# You can overload these methods to change their behavior within a class. For example, in order to use a custom implementation of the '+'
# operator, you will need to override the __add__() method.

# This practice can be useful when overriding __init__(), similar to using a constructor in a Java. For example:

class Friend:
    # Call 'self' as an argument in order to access attributes and methods in the current object, as we need to provide the instance
    # See the Resources section for more info on using the 'self' parameter
    def __init__(self,name):
        self.name = name  #like a constructor!
    
    def introduce_friend(self): # points to current object
        print("This is my friend,", self.name)
        
my_friend = Friend('Khayle')
my_friend.introduce_friend()


# V. ADDITIONAL RESOURCES
# https://data-flair.training/blogs/python-method/
# https://www.tutorialsteacher.com/python/magic-methods-in-python
# https://www.geeksforgeeks.org/self-in-python-class/
# https://www.programiz.com/article/python-self-why






