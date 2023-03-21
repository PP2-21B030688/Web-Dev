arr = [1, 5, 3, 77, 5]
cnt = 0

for i in range(len(arr)):
    if(i-1 >=0 and i+1 < len(arr)):
        if(arr[i-1] < arr[i] and arr[i+1] < arr[i]):
            cnt += 1

print(cnt)