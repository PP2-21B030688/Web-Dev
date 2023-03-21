x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

res = False

if(x2 == x1 - 2 and y2 == y1 + 2):
    res = True
elif(x2 == x1 - 2 and y2 == y1 - 1):
    res = True
elif(x2 == x1 - 1 and y2 == y1 + 2):
    res = True
elif(x2 == x1 - 1 and y2 == y1 - 2):
    res = True
elif(x2 == x1 + 1 and y2 == y1 + 2):
    res = True
elif(x2 == x1 + 1 and y2 == y1 - 2):
    res = True
elif(x2 == x1 + 2 and y2 == y1 + 1):
    res = True
elif(x2 == x1 + 2 and y2 == y1 - 1):
    res = True

if(res):
    print("YES")
else:
    print("NO")