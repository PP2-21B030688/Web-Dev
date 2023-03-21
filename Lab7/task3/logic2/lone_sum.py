def lone_sum(a, b, c):
    if(a == b == c):
        return 0
    elif(a == b):
        return c
    elif(a == c):
        return b
    elif(b == c):
        return a

print(lone_sum(3, 3, 3))    