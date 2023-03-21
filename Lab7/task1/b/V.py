a = int(input())
b = int(input())
c = int(input())

if(c == 0 and a == 0 and b == 0):
    pass
elif(a == 0 and b == 0):
    pass
elif(a == 0 and c == 0):
    print(0)
elif(b == 0 and c == 0):
    print(0)
elif(a == 0):
    print((c*-1) / b)
elif(b == 0):
    if((c*-1) / a > 0):
        print(((c*-1) / a) ** 0.5)
elif(c == 0):
    print(0)
    print((b*-1) / a)
