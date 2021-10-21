# 137 Documentation (137_documentation.py)
# US#80 Python Practice
# Task#137 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/137

# David Wingard
# SER401 Capstone
# Version 1.0

# This file demonstrates how to properly using documentation within Python files.
# Reference: https://www.python.org/dev/peps/pep-0257/

# Documentation utilizes docstrings, which is a string literal stored in the
# '__doc__' special attribute of every object.
# docstrings are used for every module, public class, function, and method.

# Docstrings use triple quotes and are placed in the first line after a module, function, class, or method definition

# I. One-Line Docstrings

# One-line docstrings are used to convey obvious cases.
# They are phrases that end in periods.
def get_name():
    """Return the name of the object."""
    ret = 'DJ'
    return ret


# One-line docstrings should not reiterate the signature of a function
def multiply(a, b):
    """multiply(a, b) -> a*b"""
    ...

# II. Multi-Line Docstrings


# Multi-line docstrings have a format for functions and methods consisting of
#   a summary, arguments, return values, etc.
def parse_data(pathname=None):
    """Retrieve and process data to JSON format.

    Keyword arguments:
    pathname -- the relative path of the file to be processed

    if pathname == None
        return empty JSON object
    else
        return JSON object
    """
    ...


# Docstrings in a class
class Pie:
    """This class represents a Pie.

    Note that there is a blank line always after the class summary. This can serve as an extra description.

    Attributes
    ----------
    filling : str
    bake_time : int

    Methods
    -------
    announce_yourself()
        Prints the type of pie it is.
    bake_longer(time=0)
        Extends the cook time of the pie.
    """

    def __init__(self, filling, bake_time=0):
        """
        Parameters
        ----------
        filling : str
            The type of filling in the pie
        bake_time : int, optional
            The amount of time the pie requires in the oven
        """
        self.filling = filling
        self.bake_time = bake_time

    def announce_yourself(self):
        """Prints the type of pie it is.

        Raises
        ------
        NotImplementedError
            If filling is None
        """
        if self.filling is None:
            raise NotImplementedError("I have no type since I have no filling!")

        response = f"I am a {self.filling} pie!"
        print(response)

    def bake_longer(self, time=0):
        """Extends the cook time of the pie.

        Parameters
        ----------
        time : int, optional
            The amount of time to add to the bake time of the pie
        """
        self.bake_time += time


# III. Other notes

# The help command can be used to see documentation
help(Pie)

# The docstring of a script should be its usage message

# The docstring of a module should contain classes, exceptions, and functions
