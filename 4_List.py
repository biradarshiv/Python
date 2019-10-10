"""
Python Collections (Arrays)

List is a collection which is ordered and changeable. Allows duplicate members. []
Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
Set is a collection which is unordered and unindexed. No duplicate members. {}
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. {"x":"y"}
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1]) # Access Items
print(thislist[-1]) # Negative Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Range of Indexes
print(thislist[-4:-1]) # Range of Negative Indexes
thislist[1] = "blackcurrant" # Change Item Value
print(thislist)

print("Loop Through a List")
for x in thislist:
  print(x)

print("Check if Item Exists")
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print(len(thislist)) # List Length

# Add Items
thislist.append("orange")
print(thislist)
# To add an item at the specified index, use the insert() method
thislist.insert(0, "orange")
print(thislist)
# Remove Item
thislist.remove("orange")
print(thislist) # This will only remove the first occurance only
# The pop() method removes the specified index, (or the last item if index is not specified)
print("The pop() method removes the specified index, (or the last item if index is not specified)")
thislist.pop()
print(thislist)
thislist.pop(0)
print(thislist)
# The del keyword removes the specified index
print("The del keyword removes the specified index")
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely
del thislist # thislist is deleted, hence cannot be used in print
print("The clear() method empties the list")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""
Copy a List
You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().
"""
print("Copy a List")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Another way to make a copy is to use the built-in method list()
mylist = list(thislist)
print(mylist)

print("Join Two Lists using +")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print("Join Two Lists using append")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

print("Join Two Lists using extend")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

print("use the list() constructor to make a new list")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""
Python has a set of built-in methods that you can use on lists.
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

