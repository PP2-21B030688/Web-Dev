n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

x = int(input())

for i in range(n-1):
    if(arr[i] >= x and x >= arr[i+1]):
        print(i+2)
        break