x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if(  ( (y1 - y2).__abs__() == (x1 - x2).__abs__() )  or (y1 == y2 or x1 == x2) ):
    print("YES")
else:
    print("NO")