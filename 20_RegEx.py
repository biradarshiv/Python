"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
"""

print('# Search the string to see if it starts with "The" and ends with "Spain"')
import re
txt = """The rain in Spain"""
x = re.search("^The.*Spain$", txt)
print(x)

print("# findall() Function")
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

print("# search() Function")
# If there is more than one match, only the first occurrence of the match will be returned:
str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())

print("# split() Function")
str = "The rain in Spain"
x = re.split("\s", str)
print(x)

print("# You can control the number of occurrences by specifying the maxsplit parameter:")
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

print("# sub() Function replaces the matches with the text of your choice")
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

print("# Replace the first 2 occurrences:")
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)


print("# Match Object")
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object

"""
The Match object has properties and methods used to retrieve information about the search, and the result:
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

print("# span")
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

print("# string")
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

print("# group - Print the part of the string where there was a match")
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.

print("# EOF")

