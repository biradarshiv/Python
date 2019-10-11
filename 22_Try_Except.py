"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

print("# try except")
try:
  print(x)
except:
  print("An exception occurred hence exception")

print("# Many Exception blocks")
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


print("# You can use the else keyword to define a block of code to be executed if no errors were raised")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("# The finally block, if specified, will be executed regardless if the try block raises an error or not")
try:
  print('Hi')
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

print("# The program can continue, without leaving the file object open")
print("# This can be useful to close objects and clean up resources")

print("# EOF")

