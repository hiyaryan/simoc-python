# 132 Object-Oriented Programming (132_object_oriented_programming.py)
# US#80    Python Practice
# Task#132 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/132?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates a simple object-oriented program.
# Reference: https://realpython.com/python3-object-oriented-programming/

# Find more information on object-oriented programming below.
# https://docs.python.org/3/tutorial/classes.html


# CONTENTS
# I.   Class Definition
# II.  Object Instantiation
# III. Inheritance


# I. CLASS DEFINITION
# Class definitions start with the keyword "class"
# Class names are written in PascalCase
class Dog:
    pass


# Note: "pass" keyword is a placeholder allowing Python to compile minimally without error

# Constructors are written using the method __init__()
# The first parameter in __init__ is the keyword "self"
#       New class instances are passed to "self" so that new "instance" attributes may be added
# Attributes are written in __init__(); they are not declared globally and are called 'instance' attributes

class Dog:
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age   # instance attribute


# Class attributes are attributes with the 'same' value for all class instances
#       They must always be assigned an initial value
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


