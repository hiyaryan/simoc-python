# 126 Variables (126_variables.py)
# US#80    Python Practice
# Task#126 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/126?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates how to make and use variables in Python
# Reference: https://realpython.com/python-variables/

# Find more information on variables below
# https://www.python.org/dev/peps/pep-0008/


# CONTENTS
# I.   Variable Assignment
# II.  Variable Types
# III. Object References
# IV.  Object Identity
# V.   Variable Names
# VI.  Reserved Words


# I. VARIABLE ASSIGNMENT
# Variables do not need to be declared of defined in advance

# Use the "=" to assign a variable to a value
n = 300

# To update a variable assign it to a new value
n = 1000

# Variables may be chained to the same value
a = b = c = 300


# II. VARIABLE TYPES
# Variables are not restricted to a type

# var is assigned a double value
var = 23.5

# var is reassigned to a string
var = "Now I'm a string"


# III. OBJECT REFERENCES
# Everything in python is an object
n = 300

# The following prints <class 'int'>
print(type(300))

# The following prints <class 'int'>
# This verifies that n points to an integer object
print(type(n))

# m is a new symbolic name that points to the same object n points to
m = n

# The following changes the object m points to
m = 400

# The following changes the object n points to and 300 is "orphaned"
n = "foo"

# Object lifetime
# An object stays alive as long as there is at least on variable referencing it.


# IV. OBJECT IDENTITY
# Objects are identified with a unique number
n = 300
m = n

# The following prints the same unique integer ID
print(id(n))
print(id(m))

# The following references the same ID as above
# This is because the interpreter optimizes the program for object of the same value
m = 300
print(id(m))


# V. VARIABLE NAMES
# The following are valid variable names
name = "Bob"
Age = 54
has_W2 = True
print(name, Age, has_W2)

# The following is not valid
# Variables cannot begin with numbers
# 11099_filed = False

# Python is case sensitive
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# Naming conventions according to PEP 8, Python Style Guide
# snake_case should be used for functions and variable names
# PascalCase should be used for class names

# Note: Difference between PascalCase and camelCase


# VI. RESERVED WORDS
# There are 33 reserved keywords (as of Python 3.6) listed below
# Reserved keywords cannot be used as variable names

# False
# None
# True
# and
# as
# assert
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield

