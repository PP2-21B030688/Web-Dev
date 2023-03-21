arr = [1, 2, 3, 4, 5]

for i in range(int(len(arr)/2)):
    temp = arr[i]
    arr[i] = arr[len(arr)-i-1]
    arr[len(arr)-1-i] = temp

print(arr)