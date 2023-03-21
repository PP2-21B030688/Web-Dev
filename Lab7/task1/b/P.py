a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = f = 0

full1 = a * 100 + b
full2 = c * 100 + d
if(full1 > full2):
    print("not enough")
elif(full1 == full2):
    print(0, 0)
else:
    diff = full2 - full1
    e = diff / 100
    f = diff % 100
    print(int(e), f)
