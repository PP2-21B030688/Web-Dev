n = int(input())

arr = set()

for i in range(n):
    arr.add(int(input()))

max = secondMax = -9999999

for i in arr:
    if(i >= secondMax):
        if(i > max):
            secondMax = max
            max = i
        else:
            secondMax = i

print(secondMax)