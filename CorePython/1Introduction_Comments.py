"""
Python is a programming language.

Python Syntax compared to other programming languages
Python was designed for readability, and has some similarities to the English language.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python uses indentation to indicate a block of code.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly brackets for this purpose.

Run below in command line
# To get to know the python version installed in our system
python --version
# Save the file containing code with an extension of .py and run it with below command
python helloworld.py

"""

# Indentation Matters
if 5 > 2:
 print("Five is greater than two!")
# Even though the indentation space is different it has to be the same to consider it as a block
# Even a single space will do as a indentation. Atleast one space should be there to start a block
if 6 > 2:
        print("Six is greater than two!")
        print("This will also print because of same indentation")

# Variables
# In Python variables are created the moment you assign a value to it. Python has no command for declaring a variable.
x = 5
y = "Hello, World!"
print(x)
print(y)

# Single line comment is # and multiline comment is in the middle of 3 double quotes
'Single line comment'
"""
Multiple
Line 
Comment
"""
