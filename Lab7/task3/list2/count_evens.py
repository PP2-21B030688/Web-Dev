def count_evens(arr):
    res = 0
    for i in arr:
        if(i % 2 == 0):
            res += 1
    return res

print(count_evens([2, 1, 2, 3, 4]))