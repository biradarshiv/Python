"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression
"""

print("# A lambda function that adds 10 to the number passed in as an argument, and print the result")
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number")
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) # here 2 is the unknown number which will be multiplied to make it double
mytripler = myfunc(3) # using the same function to triple the digit

print(mydoubler(11))
print(mytripler(11))


print("# EOF")