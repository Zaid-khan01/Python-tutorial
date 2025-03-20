# # Preview
# # 1. Syntax Error in python
# # 2. Logical Errors
# # 3. Common Built-in Exceptions
# # 4. Error handling
#
# # 1. Syntax Error in python, Ex-
# age = 26
# # if age>17       # here error comes because we don't use colon according to syntax
# #      print("You are eligible for voting")
#
# # 2. Logical error
# num1 = [1, 2, 3, 4]
# total = 0
#
# for num in num1:
#     total += num
#
# avg = total/len(num1)-1    # here program contains logical error, because average means sum upon total number
# print(avg)
#
# # 3. Common Built-in Exceptions
# # a. IndexError - When the wrong index of a list is retrieved
# # b. AssertionError - When the assert statements fails
# # c. AttributeError - When the attribute assignment is failed
# # d. ImportError - When imported module is not found
# # e. KeyError - When the key of the dictionary is not found
# # f. NameError - When variable is not found
# # g. MemoryError - When program runs out of memory
# # h. TypeError - When a function and operation are applied in an incorrect type
#
# # ----------- Error Handling --------------
# # Try, Except, Finally
#
# try:
#     numerator = int(input("Enter a number in numerator - "))
#     denominator = int(input("Enter a number in denominator - "))
#     result = numerator/denominator
#
#     print(result)
# except:
#     print("Denominator cannot be 0")
#
# finally:    # this finally block is executed either exception is occurred or not
#     print("Exception is handled successfully")
#
#
# # raising a specific exception
#
# try:
#     thisList = [1,2,3,4,5]
#     index = int(input("Enter an index - "))
#     print(thisList[index])
#
# except IndexError:
#     print("Index out of bound")
#
# finally:
#     print("Exception is handled")


# else clause - if we want to run a certain block of code, if the code block inside try runs without error
try:
    n = int(input("Enter a number - "))
    assert n%2 == 0     # assert is a condition which should always be true, if false then we have to handle it

except:
    print("Not an even number")

else:
    # if even number then we have to find it reciprocal
    reciprocal = 1/n
    print(reciprocal)

# (IMP)*** Note - else block runs without executing preceding exception block, hence it may happen that in this else block
# another exception is occurred, Ex - if we enter '0' in this program, then it is an even number hence except block won't
# execute, but in else block reciprocal of zero gives an exception - "division by zero", so we have to handle it accordingly


# Custom Exceptions - user defined exceptions which inherits from the exception class
class InvalidAgeException(Exception):
    "Raising an exception when age is less than 18"

age = 18
try:
    num = int(input("Enter an age - "))
    if num<age:
        raise InvalidAgeException
    else:
        print("Eligible for voting")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")
