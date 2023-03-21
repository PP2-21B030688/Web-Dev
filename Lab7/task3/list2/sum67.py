def sum67(arr):
    sum = 0
    section = False
    for i in arr:
        if(i == 6):
            section = True
        elif(i == 7):
            section = False
        else:
            if(not section):
                sum += i
            else:
                pass
    return sum

print(sum67([1, 2, 2, 6, 98, 41241241412, 7, 4]))