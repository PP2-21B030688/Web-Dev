def common_end(arr1, arr2):
    if(arr1[0] == arr2[0] or arr1[len(arr1)-1] == arr2[len(arr2)-1]):
        return True
    return False