thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)

# Access Tuple Items
print(thistuple[1])
# Negative Indexing
print(thistuple[-1])
# Range of Indexes
print(thistuple[2:5])
print(thistuple[-4:-1])

# Tuples are unchangeable
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Loop Through a Tuple
print("# Loop Through a Tuple")
for x in thistuple:
  print(x)

print("# Check if Item Exists")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

print("# Tuple Length")
print(len(thistuple))

print("# Create Tuple With One Item")
# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple, it is considered as string
thistuple = ("apple")
print(type(thistuple))

# add or remove from tuple is not possible since they are unchangeable

print("# Join Two Tuples")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

print("# The tuple() Constructor")
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print("# Tuple count() Method")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(8)
print(x)

print("# Tuple index() Method")
x = thistuple.index(8)
print(x)


print("# EOF")