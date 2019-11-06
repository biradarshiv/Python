"""
Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
"""

print("# iter method usage")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

print("# Strings are also iterable objects, containing a sequence of characters")
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))

print("# for loop to iterate through an iterable object")
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

print("# Create Iterator")
"""
To create an object/class as an iterator we have to implement the methods __iter__() and __next__() to our object.
All classes have a function called __init__(), which allows you do some initializing when the object is being created.
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("# Stop iteration after 20 repetitions, otherwise for loop will end in infinite loop")
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


print("# EOF")