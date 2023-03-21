def max_end3(arr):
    max = (arr[0] if arr[0] >= arr[2] else arr[2])
    return [max, max, max]

print(max_end3([1, 2, 3]))