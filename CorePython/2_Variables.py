"""
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
x=5
print(x)

x = "John"
# is the same as
x = 'John'
print(x)

# Python allows us to assign values to multiple variables in one line
print('# Python allows you to assign values to multiple variables in one line')
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# And you can assign the same value to multiple variables in one line
print('# And we can assign the same value to multiple variables in one line')
x = y = z = "Orange"
print(x)
print(y)
print(z)
#You can also use the + character to add a variable to another variable
print('You can also use the + character to add a variable to another variable')
x = "Python is "
y = "awesome"
z =  x + y
print(z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
#print(x + y) #print("This will throw error since we cannot add a number and text")

#Global and Local Variables
"""If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value."""
x = "awesome" # This is a global variable
def myfunc():
    #print("Python is " + x)
    # #Once a local variable is declared, it cannot use the global variable.
    # Use the variable only after declaration.
    x = "fantastic" # This is a local variable
    print("Python is " + x)
myfunc()
print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "global"
def myfunc():
  global x
  x = "local in function referring / pointing to global"
myfunc()
print("Now x will print the " + x)

