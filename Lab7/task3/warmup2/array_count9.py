def array_count9(arr):
    cnt = 0
    for i in arr:
        if(i == 9):
            cnt += 1
    return cnt

print(array_count9([1, 9, 9]))