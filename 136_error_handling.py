# 136 Error Handling (126_error_handling.py)
# US#80    Python Practice
# Task#136 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/136?

# Ian Castellanos
# SER401 Capstone
# Version 1.0

# Error handling is critical for catching and handling potential errors
# that may come up in program flow. This will help devs and programs to 
# to be able to properly continue without hard crashes and offer insight

# In depth dive into Errors and Exceptions from Python documentation
# Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html

# There are built-in exceptions that check for type, names, divide by 0
# and other common programming concepts

import sys

# Instance of checking for input of an Int, can be changed to other types
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    # multiple exceptions can be parenthensized as a tuple
    # except (RuntimeError, TypeError, NameError):
    except ValueError:
      print("Oops!  That was no valid number.  Try again...")

# else clauses are not handled if they are not caught
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# all builtin Exception types can be shown using this command
print(dir(locals()['__builtins__']))

# AssertionError	Raised when an assert statement fails.
# AttributeError	Raised when attribute assignment or reference fails.
# EOFError	Raised when the input() function hits end-of-file condition.
# FloatingPointError	Raised when a floating point operation fails.
# GeneratorExit	Raise when a generator's close() method is called.
# ImportError	Raised when the imported module is not found.
# IndexError	Raised when the index of a sequence is out of range.
# KeyError	Raised when a key is not found in a dictionary.
# KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete).
# MemoryError	Raised when an operation runs out of memory.
# NameError	Raised when a variable is not found in local or global scope.
# NotImplementedError	Raised by abstract methods.
# OSError	Raised when system operation causes system related error.
# OverflowError	Raised when the result of an arithmetic operation is too large to be represented.
# ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
# RuntimeError	Raised when an error does not fall under any other category.
# StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
# SyntaxError	Raised by parser when syntax error is encountered.
# IndentationError	Raised when there is incorrect indentation.
# TabError	Raised when indentation consists of inconsistent tabs and spaces.
# SystemError	Raised when interpreter detects internal error.
# SystemExit	Raised by sys.exit() function.
# TypeError	Raised when a function or operation is applied to an object of incorrect type.
# UnboundLocalError	Raised when a reference is made to a local variable in a function or method, 
# but no value has been bound to that variable.
# UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
# UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
# UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
# UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
# ValueError	Raised when a function gets an argument of correct type but improper value.
# ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.

# Exceptions inherit from BaseException
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    # raise forces a specific exception to occur
    raise

# Exceptions can be user defined using Exception Classes
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

# this can then be passed into other classes for exceptions
class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

# finally used to clean up actions and will always be executed
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# predefined clean-up actions use with statement to allow objects to be used
# in a way that ensure they are cleaned up
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")