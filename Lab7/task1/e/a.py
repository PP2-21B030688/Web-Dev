def getMin(arr):
    min = 9999999
    for i in numbers:
        if(int(i) <= min):
            min = int(i)

    return min

numbers = input().split()

print(getMin(numbers))