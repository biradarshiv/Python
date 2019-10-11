"""
A variable is only available from inside the region it is created. This is called scope.
"""

print("# the variable x is not available outside the function, but it is available for any function inside the function")
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc() # This call to the outside func also gives a call to the inside function

print("# Naming Variable")
"""
If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, one available in the global scope (outside the function) 
and one available in the local scope (inside the function):
"""
x = 300 # Global variable

def myfunc():
  x = 200 # local variable
  print(x)
myfunc()
print(x) # This will access the global variable

print("# Global Keyword")
"""
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
"""
def myfunc():
  global x
  x = 300
myfunc()
print(x)

print("# To change the value of a global variable inside a function, refer to the variable by using the global keyword")
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)


print("# EOF")