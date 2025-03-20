# the key function for working with files in python is the open() function
# the open() function takes two parameters - filename, and mode

# open a file for reading
f = open("demofile.txt", 'r')   # it is only available for readable bcz of 'r'
text = f.read()
print(text)
f.close()

# if we use 'w' instead of 'r' then it gives error because we have above function in read mode

f = open("demofile.txt", 'w')   # if we use 'w' mode then it overwrite our content
text = f.write("Hey your content is overwritten")
print(text)
f.close()

# append mode 'a'
f = open("demofile.txt", 'a')   # if we use 'a' mode then it just added this content after stored content
text = f.write("After appending, content is not overwritten")
print(text)
f.close()
# **** this write content will append again & again when we run program

# read only parts of file
f = open("demofile.txt", 'r')
text = f.read(5)    # read only first 5 letters
print(text)
f.close()


# readline() method
f = open("demofile.txt", 'r')
text = f.readline()  # read first line from file, so this function reads line by line from file
print(text)
f.close()

# by calling readline() two time, we can read first 2 lines of file

f = open("demofile.txt", 'r')
for x in f:     # by using for loop we can whole content of file without using close, and read function
    print(x)

# this can also be used to overwrite on stored content
with open("demofile.txt", 'w') as f:
    f.write("Content is again overwritten")


f = open("demofile.txt", 'r')
text = f.read()
print(text)
f.close()


