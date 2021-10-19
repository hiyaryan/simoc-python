# 135 Files (135_files.py)
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

# Additional resources
# pandas library
#   Description:
#       An open-source library that provides high performance data analysis tools and easy
#       to use data structures. This library is recommended when parsing CSV files with a lot of data.
#   Link: https://realpython.com/python-csv/#parsing-csv-files-with-the-pandas-library


# CONTENTS
# I.   Reading and Writing Files (Overview and .txt Files)
# II.  Reading and Writing .csv Files
# III. Reading, Parsing, and Writing .json Files


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

# Reading and Writing Opened Files
# Read Functions
# .read(size=-1):     reads file on number of size bytes; no arguments, None, or -1 reads the entire file
# .readline(size=-1): reads at most size number of characters from the line, no arguments, None, or -1 reads
#                     the entire line
# .readlines():       reads the remaining lines from the file and returns them as a list

# Examples
# .read()
with open('135_files/135_txt.txt', 'r') as reader:
    print(reader.read())

# .readline()
with open('135_files/135_txt.txt', 'r') as reader:
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))

# .readlines()
with open('135_files/135_txt.txt', 'r') as reader:
    print(reader.readlines())

# Additionally .readlines() can be done using list()
with open('135_files/135_txt.txt', 'r') as reader:
    print(list(reader))

# Iterating Over Each Line in the File
# Iterate using .readline() function
with open('135_files/135_txt.txt', 'r') as reader:
    # Read an print line by line
    line = reader.readline()

    # EOF is an empty string
    while line != '':
        print(line, end='')
        line = reader.readline()

# Iterate using .readlines() function
with open('135_files/135_txt.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')

# SUGGESTED: Iterate over the file object itself
with open('135_files/135_txt.txt', 'r') as reader:
    for line in reader:
        print(line, end='')

# Write Functions
# .write(string):   Writes a string to the file
# .writelines(seq): Writes the sequence to the file with no line endings

# Examples
with open('135_files/135_txt.txt', 'r') as reader:
    dog_breeds = reader.readlines()

with open('135_files/135_txt.txt', 'w') as writer:
    for breed in reversed(dog_breeds):
        writer.write(breed)

    # Alternatively the following does the same
    # writer.writelines(reversed(dog_breeds))

# __file__
# The relative pathname of the file from which it was loaded
with open('135_files/135_txt.txt', 'r') as reader:
    print(__file__)

# Appending to a file
# Append to a file using the mode char 'a'
with open('135_files/135_txt.txt', 'a') as writer:
    writer.write('\nBeagle')

with open('135_files/135_txt.txt', 'r') as reader:
    reader.read()

# Reading and Writing Simultaneously
d_path = '135_files/135_txt.txt'
d_r_path = '135_files/135_txt_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))


# Context Managers
# Provides finer control of object files
# Object files should be placed inside a custom clas

class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    # __enter__ is equivalent to using a with statement
    # In this Context Manager the file can open with additional functionality
    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    # __exit__ is equivalent to exiting a with statement block
    # In this Context Manager the file can exit with additional functionality
    def __exit__(self, type, val, tb):
        self.__file_object.close()

    # Additional methods here as required.


# Use the Context Manager class in the same fashion as the with statement
with my_file_reader('135_files/135_txt.txt') as reader:
    # Perform custom class operations
    pass


# II. READING AND WRITING CSV FILES
# Import csv library to access functionality to read and write CSV files
import csv

# OPTION 1: Process the CSV file as a list of String elements
with open('135_files/135_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1

    print(f'Processed {line_count} lines.')

# OPTION 2: Process the CSV into a dictionary
with open('135_files/135_csv.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1

    print(f'Processed {line_count} lines.')


# Optional CSV reader Parameters
# delimiter:  character separating each field; default=',' comma
# quotechar:  character used to surround fields containing the delimiter; default='"' quote
# escapechar: character used to escape the delimiter character if no quotes are used; default=no escape character

# Writing CSV Files with csv library
with open('135_files/135_csv.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


# Optional quoting={} parameter:
# 1. QUOTE_MINIMAL: quote fields only containing the delimiter
# 2. QUOTE_ALL: quote all fields
# 3. QUOTE_NONNUMERIC: quote fields containing text, convert all numeric fields to float types
# 4. QUOTE_NONE: escape delimiters, must provide value for escapechar optional parameter

# Writing CSV from a Dictionary
with open('135_files/135_csv.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

# Note: pandas library is an open-source library that provides high performance data analysis tools and easy
# to use data structures. This library is recommended when parsing CSV files with a lot of data.
# Reference: https://realpython.com/python-csv/#parsing-csv-files-with-the-pandas-library


# III. READING, PARSING, AND WRITING JSON FILES
