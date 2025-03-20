# 1. if-else
a = 3
b = 4
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

# if i want to check 3 integer, which one is greater
a, b, c = 10, 30, 9
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")

#. elif
x, y = 30, 30
if x>y:
    print("x is greater than y")
elif x==y:
    print("x and y are equal")
else:
    print("y is greater than a")
