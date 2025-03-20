
# len() function is an example of function polymorphism

x = "Hello world"
print(len(x))

thisList = ["Apple", "Mango","Apple", "Orange"]
print(len(thisList))    # in this len() function returns elements of list

thisTuple = ("Apple", "Mango", "Mango", "Orange")
print(len(thisTuple))   # len() returns number of items in tuple

dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2019
}
#print(len(dict))    # len() function returns number of keys


# Function polymorphism
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self,name, model):
        self.name = name
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self,name, model):
        self.name = name
        self.model = model

    def move(self):
        print("Fly")

x1 = Car("Ford", "Mustang")
x2 = Boat("IndianSea", 50)
x3 = Plane("Air India", "Model 27")

for x in (x1, x2, x3):
    x.move()