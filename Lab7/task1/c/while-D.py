n = int(input())
pow = 1

while(pow < n):
    if(pow == n):
        break

    pow *= 2

if(pow == n):
    print("YES")
else:
    print("NO")