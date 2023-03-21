def array123(arr):
    cnt = 0
    for i in arr:
        if(cnt == 0 and i == 1):
            cnt += 1
        elif(cnt == 1 and i == 2):
            cnt += 1
        elif(cnt == 2 and i == 3):
            return True
    return False

print(array123([1, 1, 2, 4, 1]))