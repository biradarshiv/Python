"""
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
"""

print("# we can use the module we created, by using the import statement")
import mymodule
mymodule.greeting("Jonathan")
# Note: When using a function from a module, use the syntax: module_name.function_name.

print("# Accessing a dictionary from another module")
a = mymodule.person1["age"]
print(a)

print("# Re-naming a Module")
# create an alias when you import a module, by using the as keyword
# Create an alias for mymodule called mx
import mymodule as mx

a = mx.person1["age"]
print(a)

print("# There are several built-in modules in Python, which we can import whenever we like")
import platform
x = platform.system()
print(x)

print("# dir() Function")
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
import platform
x = dir(platform)
print(x)

print("# You can choose to import only parts from a module, by using the from keyword")
from mymodule import person1
print (person1["age"])
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]

print("# EOF")

