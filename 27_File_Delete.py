"""
To delete a file, you must import the OS module, and run its os.remove() function:
"""

print("# Delete a File")
import os
os.remove("demofile2.txt")

print("# Check if File exist, and then delete it")
import os
if os.path.exists("demofile3.txt"):
  os.remove("demofile3.txt")
else:
  print("The file does not exist")

print("# Delete Folder")
# To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("myfolderjunk")


print("# EOF")

