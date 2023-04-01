arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
cnt = 0

for i in range(1, len(arr)):
    if(arr[i] > arr[i-1]):
        cnt += 1

print(cnt)