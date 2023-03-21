def first_last(arr):
    if(arr[0] == 6 or arr[len(arr)-1] == 6):
        return True
    return False

print(first_last([1, 6, 4]))