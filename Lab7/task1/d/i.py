n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

carry = arr[0]

for i in range(n-1):
    temp = arr[i+1]
    arr[i+1] = carry
    carry = temp

arr[0] = carry

print(arr)