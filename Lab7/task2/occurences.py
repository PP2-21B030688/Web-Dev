s = input()
x = input()

cnt = 0

for i in range(len(s)):
    if(s[i:i+len(x)] == x):
        cnt += 1

print(cnt)