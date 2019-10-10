"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("# Accessing Items")
x = thisdict["model"]
print(x)
# There is also a method called get() that will give you the same result
x = thisdict.get("model")
print(x)

print("# Change or set Values")
thisdict["year"] = 2018

print("# Loop Through a Dictionary")
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
print("# Print Keys")
for x in thisdict:
  print(x)
print("# Print values")
for x in thisdict:
  print(thisdict[x])
print("# use the values() function to return values of a dictionary")
for x in thisdict.values():
  print(x)
print("# Loop through both keys and values, by using the items() function")
for x, y in thisdict.items():
  print(x, y)
print("# Check if Key Exists")
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("# Dictionary Length")
print(len(thisdict))

print("# Adding Items")
thisdict["color"] = "red"
print(thisdict)

print("# Removing Items")
thisdict.pop("model")
print(thisdict)

print("# The del keyword removes the item with the specified key name")
del thisdict["color"]
print(thisdict)

print("# The del keyword can also delete the dictionary completely")
del thisdict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("# The clear() keyword empties the dictionary")
thisdict.clear()
print(thisdict)

print("# Copy a Dictionary")
"""
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print("# Make a copy of a dictionary with the dict() method")
mydict = dict(thisdict)
print(mydict)

print("# Nested Dictionaries")
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

print("# Create three dictionaries, than create one dictionary that will contain the other three dictionaries")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


print("# dict() Constructor")
# It is also possible to use the dict() constructor to make a new dictionary
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

print("# The fromkeys() method returns a dictionary with the specified keys and values.")
x = ('key1', 'key2', 'key3')
y = (0)
thisdict = dict.fromkeys(x, y)
print(thisdict)

print("# EOF")

"""
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

print("# EOF")