# 123 Syntax and Naming Standards (123_syntax_naming_standards)
# US#80    Python Practice
# Task#123 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/123?

# Ryan Meneses
# SER401 Capstone
# Version 1.0

# This file demonstrates Python syntax and naming standards.
# Reference: https://jakevdp.github.io/WhirlwindTourOfPython/02-basic-python-syntax.html

# In general, follow the style guidelines as laid out in PEP-8
# https://www.python.org/dev/peps/pep-0008/


# **** CONTENTS ****
# I.   Comments
# II.  Statement Terminates
# III. Indentation
# IV.  Parenthesis
# V.   Naming Conventions


# I. COMMENTS
# 1. Comments begin with the hash '#' symbol

# 2. Comments may be inline
x = 0
x += 2  # shorthand for x = x + 2

# 3. No syntax for multiline comments


# II. STATEMENT TERMINATES
# 1. End-of-Line Terminates the Statement (semicolon is optional ';')
count = 7

lower = []; upper = []
# Equivalent to
lower = []
upper = []

# 2. To spread a statement over multiple lines use '\' or surround in parenthesis '()'
x = 1 + 2 + 3 + 4 + \
    5 + 6 + 7 + 8

x = (1 + 2 + 3 + 4 +
     + 5 + 6 + 7)


# III. INDENTATION
# 1. Whitespace sensitive
for i in range(10):
    # indentation represents a code block
    if i < x:
        lower.append(i)
    else:
        upper.append(i)

# 2. Indented code blocks are always preceded by a colon ':'
total = 0;
for i in range(100):
    total += i

# 3. Amount of indentation for a code block is up to user
# This example is the same as 1. above
for i in range(10):
            if i < x:
                    lower.append(i)
            else:
                    upper.append(i)

# 4. Whitespace within a single line does not matter
x=1+2
x = 1 + 2
x           =           1           +           2


# IV. PARENTHESIS
# 1. Parenthesis are for grouping
x = 2 * (3 + 4)

# 2. Parenthesis indicate a function is being called
# 2.1Calling a function with arguments
print('1st value', 1)
print('2nd value', 2)

# 2.2 Calling a function without arguments
L = [4, 2, 3, 1]
L.sort()


# V. NAMING CONVENTIONS
# 1. Names to Avoid
# Never use l/L or O (letter "oh") as single variable names
l = "Do not use l as a single variable name!"
L = "Do not use L as a single variable name!"
O = "Do not use O as a single variable name!"

# 2. Package and Module Names
# 2.1 Module names are short, all-lowercase, and uses underscores as necessary for readability
some_module = "Module naming convention."

# 2.2 Package names are short, all-lowercase, and discourages the use of underscores
package = "Package naming convention."

# 3. Class Names
# Class names use the CapWord (camelcase) convention
ClassName = "Class naming convention."

# 4. Exception Names
# Use CapWord and end it with Error (or the type of exception)
StackOverflowError = "Error naming convention."
SocketException = "Exception naming convention."

# 5. Global and Function Variables
# Global and Function variables should be lowercase with words separated by underscores
this_is_a_variable = "This is a properly named Global and Function variable."

# 6. Method Names and Instance Variables
# 6.1 Same as function naming rules
some_public_method = "Public method naming convention."

# 6.2 Use one leading underscore for non-public methods and instance variables
_some_private_method = "Private or protected method naming convention."

# 7. Constants
# Constants should be all caps with words separated by underscores
MAX_OVERFLOW = "Constant naming convention."