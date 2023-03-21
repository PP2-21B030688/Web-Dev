x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if( (x1 - x2).__abs__() == 1 and (y1 - y2).__abs__() == 1 ):
    print("YES")
else:
    print("NO")