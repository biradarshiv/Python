"""
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
"""

print("# Parse JSON - Convert from JSON to Python")
# The result will be a Python dictionary.
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print(y)

print("# Convert from Python to JSON")
# You can convert Python object, into a JSON string by using the json.dumps() method.
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

print("# Convert Python objects into JSON strings, and print the values")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
"""

print("# Real time usage")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print("# To make the stirng readable with an indentation of 4")
print(json.dumps(x, indent=4))
print('# define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values')
print(json.dumps(x, indent=4, separators=(". ", " = ")))


print("# Order the Result based on the keys")
print(json.dumps(x, indent=4, sort_keys=True))

print("# EOF")