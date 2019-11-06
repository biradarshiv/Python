# A Set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Cannot access the elements using index, only a general for loop would work to access all elements
for x in thisset:
  print(x)

print("# check an element existing in a set")
print("banana" in thisset)

print("Once a set is created, we cannot change its items, but we can add new items.")
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes", "banana"])
print(thisset)


print("# Length of a Set")
print(len(thisset))

print("# Remove Item")
# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
print(thisset)
thisset.discard("cherry")
print(thisset)
# Note: Sets are unordered, so when using the pop() method, you will not know which item that gets remove
x = thisset.pop()
print(x + " - This is removed")
print(thisset)

print("# The clear() method empties the set")
thisset.clear()
print(thisset)

print("# The del keyword will delete the set completely")
del thisset
# print(thisset)

print("# Join Two Sets")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, "a"}
set3 = set1.union(set2)
print(set3)
print("# The update() method inserts the items in set2 into set1")
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.

print("# set() Constructor")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print("#  symmetric_difference() Method")
# returns a set that contains all items from both set, but not the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"apple", "google", "microsoft"}
z = x.symmetric_difference(y)
print(z)

print("# symmetric_difference_update() Method")
# method updates the original set by removing items that are present in both sets, and inserting the other items.
x.symmetric_difference_update(y)
print(x)


print("# EOF")

"""
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""

