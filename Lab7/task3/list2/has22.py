def has22(arr):
    for i in range(len(arr)-1):
        if(arr[i] == 2 and arr[i + 1] == 2):
            return True
    return False

print(has22([1, 2, 1, 2]))