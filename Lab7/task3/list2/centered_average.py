def centered_average(arr):
    min = 9999999
    max = -999999
    sum = 0
    for i in arr:
        if(i <= min):
            min = i
        if(i >= max):
            max = i
        sum += i
    return int((sum - max - min) / (len(arr) - 2))

print(centered_average([1, 2, 3, 4, 100]))