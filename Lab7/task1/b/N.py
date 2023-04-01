a = int(input())
b = int(input())
if(a == 0 or b == 0):
    print("INF")
elif(int((b*-1) / a) == (b*-1) / a):
    print("YES")
else:
    print("NO")