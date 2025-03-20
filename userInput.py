# name = input("Enter your name = ")
# print("Hello",name,"! Welcome!")

def sum(num1, num2):
    return num1+num2

n1 = int(input("Enter first number = "))
n2 = int(input("Enter first number = "))
print("Sum = ", sum(n1, n2))

# print number from 1 to n
def my_fun(n):
    for x in range(1, n+1):
        print(x)

n = int(input("Enter a limit = "))
my_fun(n)
