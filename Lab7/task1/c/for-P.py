a = int(input())
b = int(input())
c = int(input())
d = int(input())

res = []

for i in range(1001):
    if( ( a * (i ** 3) + b * (i ** 2) + c * i + d ) == 0 ):
        res.append(i)

for i in res:
    print(i, end=" ")