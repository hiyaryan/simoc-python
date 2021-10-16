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


# II. OBJECT INSTANTIATION
# 1. Instantiate an object by calling the class name followed by parenthesis
# Dog() # Traceback error due to missing arguments

# Assign an object to a variable using the "=" symbol
# a = Dog()
# b = Dog()
# a == b # False; a and b refer to different locations in memory


# 2. Pass arguments to the instance attributes in the parenthesis
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# The parameter "self" does not require an argument
# When a new object is created the first parameter

# Access instance attributes using dot notation
print(f"{buddy.name}, {buddy.age}")
print(f"{miles.name}, {miles.age}")

# Access class attributes using dot notation
# Access instance attributes using dot notation
print(f"{buddy.species}")
print(f"{miles.species}")


# Dynamically change instance and class attributes using dot notation
buddy.age = 10
miles.age = 5

print(f"{buddy.name}, {buddy.age}")
print(f"{miles.name}, {miles.age}")

miles.species = "Felis silvestris"
print(f"{buddy.species}")
print(f"{miles.species}")

# Key Takeaway: Custom objects are mutable

# 3. Instance methods are defined inside a claas
# The first parameter is always "self"


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method #1
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instance method #2
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Access instance methods using dot notation
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.description())
print(buddy.speak("Woof woof"))

print(miles.description())
print(miles.speak("Bow wow"))

# Print the location of an object in memory by passing the name of the object
print(miles)
print(buddy)

# To change what prints when passing the object to the print function set the "__str__" method in the class


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ sets the string representation of the object
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# The "__str__" method is set and passing an object to print now outputs the string representation of the object
print(miles)
print(buddy)

# Other dunder "double underscore: __" methods can be used to customize classes
# More information here https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/


# III. INHERITANCE
# "Inheritance is the process by which one class takes on the attributes and methods of another"
# def. Children classes: newly formed classes
# def. Parent classes: classes the children are derived from

# 1. Children classes can override or extend attributes and methods of parent classes

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # __str__ sets the string representation of the object
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9, "Jack Russell Terrier")
miles = Dog("Miles", 4, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))


# Create specific breed classes (children classes) to simplify working with the Dog class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ sets the string representation of the object
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# Put the name of the parent class in the child class parenthesis to create inheritance
class JackRusselTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


buddy = JackRusselTerrier("Buddy", 9)
miles = Dachshund("Miles", 4)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

# Determine the class an object belongs to using the built-in function "type"
print(type(miles))

# Determine if a class is an instance of another class using the built-in function isinstance
print(isinstance(miles, Dog))
print(isinstance(miles, Bulldog))
print(isinstance(jack, Dachshund))


# 2. Extend the functionality of the Parent class
class JackRusselTerrier(Dog):
    # Extends functionality of parent class with default sound attribute "Arf"
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


miles = JackRusselTerrier("Miles", 4)
# Pass no arguments and return a predefined default value
print(miles.speak())

# Pass an argument and override the default value
print(miles.speak("Grrr"))

# Note that changes to methods in the parent class propagates to children classes if the methods are not overridden
# To access the parent method that was overridden use the "super" keyword
print(miles.speak())


class JackRusselTerrier(Dog):
    # Extends functionality of parent class with default sound attribute "Arf"
    def speak(self, sound="Arf"):
        return super().speak(sound)


print(miles.speak())
