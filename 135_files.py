# 135 Files (132_files.py)
# US#80    Python Practice
# Task#135 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/135?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates a simple object-oriented program.
# Reference: Overview/.txt https://realpython.com/read-write-files-python/
#            .csv Files    https://realpython.com/python-csv/
#            .json Files   https://realpython.com/python-json/

# Find more information on reading and writing files below.
# Overview:   https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# .csv Files  https://docs.python.org/3/library/csv.html
# .json Files https://docs.python.org/3/library/json.html


# CONTENTS
# I.   Reading and Writing Files (Overview and .txt Files)
# II.  Reading and Writing .csv Files
# III. Reading, Parsing, and Writinging .json Files


# I. READING AND WRITING FILES
# To open a file invoke the built-in "open" function

# open() has a two arguments: the file path, and the mode (view below for mode example)
file = open('135_files/135_txt.txt', 'r')

# Reminder: Always close files to prevent resource leaks
# App termination will eventually close a file but when is not certain

# Close a file in two ways
# 1. Close with try/finally and the close() function
try:
    # process file contents
    print(file.read())
finally:
    file.close()

# 2. Close using a "with" statement
# The "with" statement automatically closes a file once the program exits the block of code
with open('135_files/135_txt.txt') as reader:
    # process file contents
    print(reader.read())


# Second argument of open() function: mode
# Mode is a string that may take multiple chars: default is 'r'
# It describes how the file should be opened

with open('135_files/135_txt.txt', 'r') as reader:
    # process file contents
    print(reader.read())

# List of modes
# 'r':  Open for reading (default)
# 'w':  Open for writing, truncating (overwriting) the file first
# 'rb': Open for reading in binary mode
# 'wb': Open for writing in binary mode

# def. File object--an object exposing a file-oriented API to an underlying source
# Categories of file objects:
#   1. Text Files
#   2. Buffered binary files
#   3. Raw binary files

# 1. Text File Types
# These files are open as follows
file = open('135_files/135_txt.txt') # default mode: "r"
file.close()

file = open('135_files/135_txt.txt', 'r')
file.close()

# file = open('135_files/135_txt.txt', 'w')
# file.close()

# The object returns from open() is a TextIOWrapper file object
file = open('135_files/135_txt.txt')
print(file)
file.close()

# 2. Buffered Binary File Types
# These files are open as follows
file = open('135_files/135_txt.txt', 'rb')
file.close()

# file = open('135_files/135_txt.txt', 'wb')
# file.close()

# The object returns from open() a BufferedReader or BufferedWriter file object
file = open('135_files/135_txt.txt', 'rb')
print(file)
file.close()

# file = open('135_files/135_txt.txt', 'wb')
# print(file)
# file.close()

# 3. Raw File Types
# These files are open as follows
file = open('135_files/135_txt.txt', 'rb', buffering=0)
file.close()

# The object returns from open() a FileIO file object
file = open('135_files/135_txt.txt', 'rb', buffering=0)
print(file)
file.close()