# 2 primitive loops types -
# 1. while loop
# 2. for loop

# 1. while loop
i = 1
while i<6:
    print(i)
    i+=1    # i++ is not available in python

# 2. for loop
fruits = ["apple", "banana", "mango"]
for x in fruits:    # print each value present in list-fruits
    print(x)

for i in "ZAID KHAN":   # print each letter present in word ZAID KHAN
    print(i)

# range function
for x in range(6):  # prints number from 0 by default to range-1 = 5
    print(x)

for x in range(1,5):    # prints number from 1 to range-1 = 4
    print(x)

# by third parameter in range() function it increments the range by that 3rd parameter
for x in range(1, 11, 2):
    print(x)