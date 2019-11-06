"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""
print("# Parent Class")
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

print("# Child Class")
# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:

class Student(Person):
  pass
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
x = Student("Mike", "Olsen")
x.printname()

print("# Using Super and adding attribute in the child")
"""
super() function that will make the child class inherit all the methods and properties from its parent:
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
      print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()
print(x.graduationyear)
x.welcome()


print("# EOF")
