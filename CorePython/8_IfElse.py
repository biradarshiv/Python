"""
Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
Other programming languages often use curly-brackets for this purpose.
"""

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# Note : You can also have an else without the elif

a = 34
b = 33
print("# Short Hand If")
# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

print("# Short Hand If ... Else")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

print("# use and / or in the if condition")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")

print("# EOF")
