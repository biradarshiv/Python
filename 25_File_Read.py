"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt")
f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.
"""

print("# Read full file")
f = open("demofile.txt", "r")
print(f.read())

print("# Read Only Parts of the File. Return the 5 first characters of the file")
f = open("demofile.txt", "r")
print(f.read(5))

print("# You can return one line by using the readline() method")
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print("# Loop through the file line by line")
f = open("demofile.txt", "r")
for x in f:
  print(x)

print("# Close the file when you are finish with it")
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

print("# EOF")