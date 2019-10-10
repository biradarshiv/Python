"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

function is defined using the def keyword
To call a function, use the function name followed by parenthesis:
"""
def my_function():
  print("Hello from a function")
my_function()

print("# Functions with in Parameters")
def my_function(fname, lname):
  print(fname + ' ' + lname)
my_function("Emil","Wow")
my_function("Tobias", "Cow")

print("# Default Parameter Value")
# If we call the function without parameter, it uses the default value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function()

print("# Passing a List as a Parameter")
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

print("# Return Values")
def my_function(x):
  return 5 * x
print(my_function(3))

print("# Keyword Arguments")
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("# Arbitrary Arguments")
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly
def my_function(*kids):
  print("The youngest child is " + kids[2])
  print("The first listed item is " + kids[0])
my_function("Emil", "Tobias", "Linus")

print("# Recursion")
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

print("# EOF")