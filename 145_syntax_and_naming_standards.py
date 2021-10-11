# 145 Syntax and Naming Standards (145_syntax_naming_standards)
# US#80    Python Practice
# Task#145 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/123?

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
# Parenthesis are for grouping
x = 2 * (3 + 4)

# Parenthesis indicate a function is being called
# Calling a function with arguments
print('1st value', 1)
print('2nd value', 2)

# Calling a function without arguments
L = [4, 2, 3, 1]
L.sort()