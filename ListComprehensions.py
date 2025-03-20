# Based on an existing list, we want to create a new list is called List comprehension
# for ex - we have a list of fruits, we want a new list where fruits name contains letter "a"

fruits = ["apple", "mango", "grapes", "kiwi", "cherry"]
newList = []
# list comprehension without list comprehension syntax
for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# using list comprehension syntax
fruits = ["apple", "kiwi", "grapes", "cherry", "orange"]
newList = [x for x in fruits if "a" in x]
print(newList)


newList = [x for x in range(10) if x<6]
print(newList)

newList = [x for x in range(10) if x%2==0]
print(newList)

newList = [x.upper() for x in fruits if "a" in x]
print(newList)

newList = ["hello" for x in fruits]
print(newList)

newList = [x if x!="apple" else "mango" for x in fruits]
print(newList)       # return the item if it is not apple, if it is apple then return mango