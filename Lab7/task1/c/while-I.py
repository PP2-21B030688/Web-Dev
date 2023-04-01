n = int(input())

f1 = 0
f2 = 1
f3 = 1
i = 1

while(f3 < n):
    f3 = f1 + f2        # 0 1 1 2 3 5 8
    f1, f2 = f2, f3
    i += 1

if(f3 == n):
    print(i)
else:
    print(-1)