# declaring a function
def my_fun():
    print("Hello from a function")

# calling a function
my_fun()

# WAP to print sum of 2 numbers passed in a function
def sum(a,b):
    s = a+b
    print("Sum = ",s)

sum(1,4)

# if the number of arguments is unknown, then add * before parameter
def my_function(*heroes):
    print("Hero name = " + heroes[1])

my_function("Superman", "Spiderman", "Batman")

# keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is = " + child3)

my_function(child1 = "Raiyan", child2 = "Arham", child3 = "Hamza")

# if the number of keyword arguments are unknown, then add ** before parameter
def my_fun(**kid):
    print("His last name is = " + kid["lname"])

my_fun(fname = "Zaid", lname = "khan")

# default parameter value
def fun(country = "UAE"):
    print("I am from "+ country)

fun("India")
fun("America")
fun()
fun("London")

# if we want to print number from 1 to given range
def fun(n):
    for x in range(1,n+1):
        print(x)

fun(6)

# if we want to check that passed number is even or odd
def fun(n):
    if n%2==0:
        print(n, "is an even number")
    else:
        print(n, "is an odd number")

num = int(input("Enter a number = "))
fun(num)


# return values
def my_fun(a,b):
    return a*b

print(my_fun(3,5))