arr = [1, 1, 3, 4, 5]
cnt = 1

for i in range(len(arr)-1):
    if(arr[i] != arr[i+1]):
        cnt+=1

print(cnt)