def same_first_last(arr):
    if(len(arr) >= 1 and arr[0] == arr[len(arr)-1]):
        return True
    return False

print(same_first_last([1, 2, 3, 1]))