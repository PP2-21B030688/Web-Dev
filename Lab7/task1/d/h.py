arr = [1, 2, 3, 4, 5, 6]

for i in range(0,len(arr)-1,2):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp

print(arr)