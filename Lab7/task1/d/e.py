arr = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 12]
found = False

for i in range(1, len(arr)):
    if(arr[i] == arr[i-1]):
        found = True
        break

print("YES" if found else "NO")