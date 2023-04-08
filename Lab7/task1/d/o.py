n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

# 1 2 2 3 3 3 2

res = 0
hasEquals = True

while(hasEquals):
    cnt = 1
    localDict = {}
    hasEquals = False
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1]):
            cnt += 1
        else:
            if(cnt >= 3):
                localDict[arr[i]] = cnt
                res += cnt
                hasEquals = True
            cnt = 1
    if(cnt >= 3):
        localDict[arr[i]] = cnt
        res += cnt
        hasEquals = True
    arr = list(filter(lambda num: num not in localDict, arr))
    
print(res)