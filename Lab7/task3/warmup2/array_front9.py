def array_front9(arr):
    for i in range(4):
        if(arr[i] == 9):
            return True
    return False

print(array_front9([1,2,3,4,9]))