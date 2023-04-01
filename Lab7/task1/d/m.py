n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = []

for i in range(1,n+1):
    arr.append(i)

# 1 2 3 4 5 6 7 8 9

diff = 0
for i in range(a-1, int((b-a)/2) + a):
    temp = arr[i]
    arr[i] = arr[b-diff-1]
    arr[b-diff-1] = temp
    diff += 1

diff = 0
for i in range(c-1, int((d-c)/2) + c):
    temp = arr[i]
    arr[i] = arr[d-diff-1]
    arr[d-diff-1] = temp
    diff += 1

print(arr)