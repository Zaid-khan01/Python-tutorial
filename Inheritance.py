# pass - when we do not want to add any other properties
# parent class


class IPU:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# child class
class Msi(IPU):
     def __str__(self):
         return f"Name = {self.name}, Age = {self.age}"

x = Msi("Zaid", 20)
print(x)

# call parent class function
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Zaid", "khan")
x.printName()

# we can also use "super()" to print parent class function

# add a new parameter in child class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, graduation_year):
        Person.__init__(self, fname, lname)
        self.graduation_year = 2027
x = Student("Zaid", "khan", 2027)
print(x.graduation_year)


