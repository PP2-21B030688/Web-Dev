def big_diff(arr):
    min = 9999999
    max = -999999
    for i in arr:
        if(i <= min):
            min = i
        if(i >= max):
            max = i
    return max - min

print(big_diff([10, 3, 5, 6]))