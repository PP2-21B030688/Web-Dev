n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

x = int(input())

if(x > 0):   # to the right
    arr.reverse();
    for i in range(int(x/2)):
        temp = arr[x-1-i]
        arr[x-1-i] = arr[i]
        arr[i] = temp

    m = int(n / 2) + x - 1
    j = 0
    for i in range(x, m):
        temp = arr[n-j-1]
        arr[n-j-1] = arr[i]
        arr[i] = temp
        j += 1

else:        # to the left
    arr.reverse();
    x *= -1
    x = n - x
    for i in range(int(x/2)):
        temp = arr[x-1-i]
        arr[x-1-i] = arr[i]
        arr[i] = temp

    m = int(n / 2) + (n - x) - 1
    j = 0
    for i in range(x, m):
        temp = arr[n-j-1]
        arr[n-j-1] = arr[i]
        arr[i] = temp
        j += 1

print(arr)