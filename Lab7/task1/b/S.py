def getSign(n):
    if(n < 0):
        return "-"
    return "+"

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if(getSign(x1) == getSign(x2) and getSign(y1) == getSign(y2)):
    print("YES")
else:
    print("NO")