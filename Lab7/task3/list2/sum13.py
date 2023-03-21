def sum13(arr):
    sum = 0
    thirteen = False
    for i in arr:
        if(not thirteen):
            if(i != 13):
                sum += i
            else:
                thirteen = True
        else:
            thirteen = False
            pass
    return sum

print(sum13([1, 13, 2, 1]))