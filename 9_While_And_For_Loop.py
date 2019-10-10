print("# while Loop")
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

print("# With the break statement we can stop the loop even if the while condition is true")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("# With the continue statement we can stop the current iteration, and continue with the next")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("# With the else statement we can run a block of code once when the condition no longer is true")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("#-----------------------------------------------")
print("# For Loops")
print("#-----------------------------------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("# Looping Through a String")
for x in "banana":
  print(x)

print("# The break Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("# continue Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("# Range() Function")
"""
The range() function returns a sequence of numbers, 
starting from 0 by default, and increments by 1 (by default), 
and ends at a specified number.
"""
for x in range(6):
  print(x) # this will print 0 to 5

print("# Range with start, End parameters")
for x in range(2, 6):
  print(x)

print("# Range with start, End, Increment parameters")
for x in range(2, 30, 3):
  print(x)

print("# The else keyword in a for loop specifies a block of code to be executed when the loop is finished")
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("# Nested Loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


print("# EOF")

