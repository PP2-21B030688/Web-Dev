s = input()
n = int(input())

arr = []
x = ""
cnt = 0

for i in range(len(s)):
    if(cnt >= n):
        arr.append(x)
        cnt = 0
        x = ""
    cnt += 1
    x += s[i]

if(cnt != 0):
    arr.append(x)

print(arr)