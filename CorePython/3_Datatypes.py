"""
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

Getting the Data Type
You can get the data type of any object by using the type() function
In Python, the data type is set when you assign a value to a variable
"""
x = "Hello World"	#str
print(type(x))
x = 20	#int
print(type(x))
x = 20.5	#float
print(type(x))
x = 1j	#complex
print(type(x))
x = ["apple", "banana", "cherry"]	#list
print(type(x))
x = ("apple", "banana", "cherry")	#tuple
print(type(x))
x = range(6)	#range
print(type(x))
x = {"name" : "John", "age" : 36}	#dict
print(type(x))
x = {"apple", "banana", "cherry"}	#set
print(type(x))
x = frozenset({"apple", "banana", "cherry"})	#frozenset
print(type(x))
x = True	#bool
print(type(x))
x = b"Hello"	#bytes
print(type(x))
x = bytearray(5)	#bytearray
print(type(x))
x = memoryview(bytes(5))	#memoryview
print(type(x))


#Setting the Specific Data Type
#If you want to specify the data type, you can use the following constructor functions
print("Setting the Specific Data Type")
x = str("Hello World")	#str
print(x)
x = int(20)	#int
print(x)
x = float(20.5)	#float
print(x)
x = complex(3+1j)	#complex example 1j    or    3+4j     or    x+jy  where x and y are numbers
print(x)
x = list(("apple", "banana", "cherry"))	#list
print(x)
x = tuple(("apple", "banana", "cherry"))	#tuple
print(x)
x = range(6)	#range
print(x)
x = dict(name="John", age=36)	#dict
print(x)
x = set(("apple", "banana", "cherry"))	#set
print(x)
x = frozenset(("apple", "banana", "cherry"))	#frozenset
print(x)
x = bool(10)#bool  # Same True is the output for   bool(True)  case sensitive
print(x)
x = bytes(4)	#bytes
print(x) # b'\x00\x00\x00\x00'
x = bytearray(5)	#bytearray
print(x) # bytearray(b'\x00\x00\x00\x00\x00')
x = memoryview(bytes(10))	#memoryview
print(x) # <memory at 0x0000000001D8D348>


x = 5
y = "10"
print(x + int(y)) # Internal conversion does not happen so I have to manually convert it to int

# bytes usage 1 - Convert string to bytes
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr) # b'Python is interesting.'

# bytes usage 2 - Create a byte of given integer size
size = 5
arr = bytes(size)
print(arr) # b'\x00\x00\x00\x00\x00'

# bytes usage 3 - Convert iterable list to bytes
rList = [1, 2, 3, 4, 5]
arr = bytes(rList)
print(arr)  # b'\x01\x02\x03\x04\x05'

"""
The bytes() method returns a immutable bytes object initialized with the given size and data. 
The bytes() method returns a bytes object which is an immmutable (cannot be modified) 
sequence of integers in the range 0 <=x < 256. 
If you want to use the mutable version, use bytearray() method.
"""

# Python has a built-in module called random that can be used to make random numbers
import random
print("Random Number with the range of 1 to 10 is - " + str(random.randrange(1,10)))


#Type Casting
print("#Type Casting")
x = int(1)   # x will be 1
print(x)
x = int(2.8) # y will be 2
print(x)
x = int("3") # z will be 3
print(x)


x = float(1)     # x will be 1.0
print(x)
x = float(2.8)   # y will be 2.8
print(x)
x = float("3")   # z will be 3.0
print(x)
x = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
print(x)
x = str(2)    # y will be '2'
print(x)
x = str(3.0)  # z will be '3.0'
print(x)

# You can assign a multiline string to a variable by using three quotes
x = """This is
a 
multiline String"""
print(x)

"""Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string."""
a = "Hello, World!"
print(a[0])
print(a[1])
print("Get the characters from position 2 to position 5 (not included)")
print(a[2:5]) # llo
print(a[-5:-2]) # orl
print(len(a)) # 13
print(a.strip()) # "Hello, World!"  # Strips the leading and trailing whitespaces
print(a.lower())
print(a.upper())
print(a.replace("H", "J")) # Jello, World!
print(a.split()) # ['Hello,', 'World!']  # the default split happens with the whitespaces
print(a.split(",")) # ['Hello', ' World!']

print("To check if a certain phrase or character is present in a string, we can use the keywords in or not in.")
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
x = "ain" not in txt
print(x)

# String concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#The format() method takes the passed arguments, formats them to string,
# and places them in the string where the placeholders {} are

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Boolean
"""
# True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.

# False
values that evaluates to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 
Value False evaluates to False.
"""
print(bool("Hello"))
print(bool(15))
print(bool(['Str']))

# Below are for false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))

print("False is returned by objects that are made from a class with a __len__ function that returns 0 or False")
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

print("isinstance() function,  can be used to determine if an object is of a certain data type")
x = 200
print(isinstance(x, int))

print("Python Identity Operators")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("Check the is operator")
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print("Check the is not operator")
print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print("Python Membership Operators")
# Membership operators are used to test if a sequence is presented in an object
x = ["apple", "banana"]
print("banana" in x) # returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list

