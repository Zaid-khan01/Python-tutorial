# class declaration
class MyClass:
    x = 5

# object creation of class
p1 = MyClass()
print(p1.x)

# Another example of class using __init()__ function
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

p1 = Person("Zaid khan", 20)
print("Hello i am" ,p1.name ,"and i am" ,p1.age ,"yrs old")


# __str()__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name = {self.name}, Age = {self.age}"

p1 = Person("Zaid", 20)
print(p1)

# modify object properties
p1.age = 30
print(p1.age)

# delete object properties
del p1.age
# print(p1.age)   # gives error that 'age' attribute is not present

# delete objects
del p1
# print(p1.name)   # gives error that p1 is undefined or not defined