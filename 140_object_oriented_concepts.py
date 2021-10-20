# 140 Object Oriented Concepts (140_object_oriented_concepts.py)
# US#80    Python Practice
# Task#140 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/140?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates a simple object-oriented program.
# Reference: Polymorphism  https://www.programiz.com/python-programming/polymorphism
#            Abstraction   https://www.askpython.com/python/oops/abstraction-in-python
#            Encapsulation https://www.askpython.com/python/oops/encapsulation-in-python

# CONTENTS
# I.   Polymorphism
# II.  Abstraction
# III. Encapsulation


# I. POLYMORPHISM
# def. Polymorphism-the use of a single type entity to represent different types in different scenarios

# 1. Polymorphism in addition operator '+'
# '+' is a polymorphic operator; it is used for addition and concatenation
num1 = 1
num2 = 2
print(num1 + num2)

str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)


# 2. Function Polymorphism
# Some built-in functions are compatible with many data types

# 'len' function is a polymorphic function; it can accept many types such as strings, lists, dicts
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))


# 3. Class Polymorphism
# Polymorphic classes are used to generalize methods without regard to the object

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat = Cat("Kitty", 2.5)
dog = Dog("Fluffy", 4)

# The objects above are packed into a tuple and are iterated using polymorphism and a common variable
for animal in (cat, dog):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# 4. Polymorphism and Inheritance
# Methods and attributes in a parent class may be overridden by methods in its children classes
# Polymorphism provides access to overridden methods and attributes

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


# Square class inherits from Shape
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


# Circle class inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius**2


# Inheritance forces the interpreter to recognize and use overridden methods in the children classes
square = Square(4)
circle = Circle(7)
print(circle)
print(circle.fact())  # fact() is not defined in Circle, therefore the parent definition is used
print(square.fact())  # fact() is defined in Square, therefore the child definition is used
print(circle.area())


# II. ABSTRACTION
# def. Abstraction-a feature wherein the user is kept unaware of the basic implementation of a function
#      property; the user is able to view basic functionalities but the internal details are hidden

# Syntax:
# from abc import ABC
# class Abs_class(ABC):
#   # abstract methods
#   # class methods

from abc import ABC, abstractmethod


class ABCClass(ABC):
    # normal method
    def method(self):
        # method definition
        pass

    @abstractmethod
    def abs_method(self):
        # abs_method definition
        pass


# Abstraction Example
from abc import ABC, abstractmethod


class ABSClass(ABC):
    def print(self, x):
        print(f"Passed value: {x}")

    @abstractmethod
    def task(self):
        print("Inside the ABSClass task abstract method")


class TestClass(ABSClass):
    def task(self):
        print("Inside the TestClass task method")


class ExampleClass(ABSClass):
    def task(self):
        print("Inside the ExampleClass task method")


test_obj = TestClass()
test_obj.task()
test_obj.print(100)

example_obj = ExampleClass()
example_obj.task()
example_obj.print(200)

print("test_obj is an instance of ABSClass? ", isinstance(test_obj, ABSClass))
print("example_obj is an instance of ABSClass? ", isinstance(example_obj, ABSClass))


# III. ENCAPSULATION
# def. Encapsulation-a way to access required variables without providing the program full-fledged
#      access to any of those variables

# Python provides access to all variables and methods globally, therefore, encapsulation can improve control
# over input and dataflow while tightening security

# The following demonstrates how easily accessible variables are
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


person = Person('Dev', 30)
# Accessing using class methods
person.display()
# Accessing directly from outside
print(person.name)
print(person.age)


# 1. Encapsulating variables by convention
# Using a single underscore '_' tells programmers the variable must only be accessed within th scope of the class

# The following demonstrates how to represent a variable as protected
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age  # _age is a protected variable by convention

    def display(self):
        print(self.name)
        print(self._age)


person = Person('Dev', 30)
# Accessing using class methods
person.display()
# Accessing directly from outside
print(person.name)
print(person._age)  # Variable is still accessible, however, '_' tells the programmer not to access it like this


# 2. Encapsulating variables by Name Mangling
# def. Name Mangling-making a variable private by using double underscores, in which case accessing from the outside
#      throws an error; the variable is only accessible within the class it is declared

# Python interpreter rewrites any variable leading with '__' as _Classname__
# e.g. __Var is rewritten by the interpreter as __Classname__Var

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age  # _age is a protected variable by convention

    def display(self):
        print(self.name)
        print(self.__age)


person = Person('Dev', 30)
# Accessing using class methods
person.display()
# Accessing directly from outside
print(person.name)
# print(person.__age)
# The previous line throws the following error:

# Traceback (most recent call last):
#   File "/Users/Ryan/Desktop/simoc-python/140_object_oriented_concepts.py", line 263, in <module>
#     print(person.__age)  # Variable is still accessible, however, '_' tells the programmer not to access it like this
# AttributeError: 'Person' object has no attribute '__age'

# This error is thrown because the leading '__' told the interpreter to rename __age as _Classname__age, therefore,
# __age does not exist in memory effectively making the variable private


# 3. Using Getters and Setters to access private variables
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age  # _age is a protected variable by convention

    def display(self):
        print(self.name)
        print(self.__age)

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        self.__age = age


person = Person('Dev', 30)
# Accessing using class methods
person.display()
# Accessing directly from outside
person.set_age(35)
person.get_age()
