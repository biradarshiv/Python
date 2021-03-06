"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
f = open("myfile.txt", "x")
"a" - Append - will create a file if the specified file does not exist
f = open("myfile.txt", "a")
"w" - Write - will create a file if the specified file does not exist
f = open("myfile.txt", "w")
"""

print("# Append content to the file")
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

print("# overwrite the content")
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


print("# EOF")
