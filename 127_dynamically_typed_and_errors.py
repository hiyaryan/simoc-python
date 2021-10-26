# 127 Dynamically Typed and Common Errors (127_dynamically_typed_and_errors.py)
# US#127    Python Practice
# Task#127 https://tree.taiga.io/project/hiyaryan-simoc-project-29/task/127

# Meridith Greythorne
# SER401 Capstone
# Version 1.0

# This file demonstrates Python as a dynamically-typed language, and shows some of the standard errors we might encounter


# CONTENTS
#    I. What is a dynamically-typed language?
#   II. Common Python Errors
#  III. Common Coding Mistakes
#   IV. Resources


# I. WHAT IS A DYNAMICALLY-TYPED LANGUAGE?
# Python is both a Strongly-typed AND Dynamically-typed language:

#    Strong Typing:     variables have a type that matters when performing operations
#    Dynamic Typing:    type of variables are determined at runtime

# This means that when performing operations, you need to understand whether the operation is compatible with the data type you're using. E.g. no adding doubles and strings together
# with the addition operand.

my_string = "example"
my_double = 4.5
#my_sum = my_string + my_double    #This will not work!

# Being dynamically-typed also allows variables to be different data types at different times during execution. This is allowed because Python treats everything as an object-- these runtime
# objects are what have types (rather than variables having a type), which allows us to do the following:

my_example = 18
my_example = "hello"    # this is now a string!

# You can see 126_variables.py for more examples of this.


# II. COMMON PYTHON ERRORS
#        1. IndexError - Code is trying to access an index that isn't valid, e.g out-of-bounds list operations
#        2. NameError - You are trying to use a variable/function name that isn't valid, e.g. it hasn't been declared yet, or it's a misspelling
#        3. SyntaxError - Can be caused my misspellings, anything that can obscure the intent of the code. For example, if I un-comment this line it will cause a SyntaxError
#        4. IndentationError/TabError - Raised due to inconsistent or incorrect indentation, such as improperly indenting whole lines, or mixing spaces and tabs
#        5. TypeError - Function/Operation applied to object of incorrect/incompatible type, such as line 30 above, or trying to arithmetically divide a string
#        6. ValueError - Thrown when a function receives an argument of correct type but improper value, eg. int("hello")


# III. COMMON CODING MISTAKES (this is not an exhaustive list by any means)
#        1. Incorrect indentation (see error above). On a large scale, an IDE can help you address this by "tabifying" or "untabifying" your code. 
#            You will need to look up how to format your code depending on your IDE.
#        2. Scope issues - In general, try to avoid global variables (those defined in the main body of a file), as their expanded range can have unintended consequences when using or
#            importing that file. In general, try to contain variables as appropriate (only define them in the scope in which they're required).
#                SPECIAL NOTE: Python follows the LEGB rule, meaning Python looks up names in the order of: Local, Enclosed, Global, then Built-in. 
#        3. Circular Dependencies - when two or more modules depend on each other, which can cause issues with code reusability, infinite recursions, etc. For example, do not 'import module1'
#            from module2 while 'import module2' exists in module1 as well. 
#        4. Issues with binding of variables - In Python, there are technically no declarations. Variables depend on Name Binding, which sets a name as a reference to the object. 
#            And Python has 'late-binding closures', meaning that inside of a closure (nested function that refers to a value of it's surrounding function, and is returned by said
#            surrounding function), the variable values are looked up only when the inner function is called. When using closures and looping to create functions, this late-binding behavior
#            can cause undesirable outcomes, for example:

def create_multipliers():
    return [lambda x : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))
    
# This actually prints out "8,8,8,8,8" rather than the desired "0,2,4,6,8". The late binding has already set "i" above to the final value of 4, meaning the only output created is 2*4.
# The above example is courtesy of https://docs.python-guide.org/writing/gotchas/

# This is not an exhaustive list by any means, however it represents some unknown-to-us common errors when coding in Python. If you discover any other errors or problems that you are
# consistently running into, please feel free to reach out to Meridith or add them here yourself!


# IV. RESOURCES
# https://www.futurelearn.com/info/courses/python-in-hpc/0/steps/65121
# https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language
# https://www.tutorialsteacher.com/python/error-types-in-python
# https://www.geeksforgeeks.org/built-exceptions-python/
# https://www.esparkinfo.com/common-mistakes-of-python-programmers.html
# https://www.oreilly.com/library/view/python-in-a/0596001886/ch04s03.html#:~:text=In%20Python%2C%20there%20are%20no,no%20longer%20holds%20a%20reference.
# https://www.programiz.com/python-programming/closure