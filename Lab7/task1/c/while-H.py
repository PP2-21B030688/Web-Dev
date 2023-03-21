n = int(input())
n -= 1

f1 = i = 0
f2 = 1
f3 = 1

while(i < n):
    f3 = f1 + f2        # 0 1 1 2 3 5 8
    f1, f2 = f2, f3
    i += 1

print(f3)