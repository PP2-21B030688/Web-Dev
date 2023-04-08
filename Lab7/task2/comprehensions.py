x = int(input())
y = int(input())
z = int(input())
n = int(input())

res = []

for i in range(z+1):
    for j in range(y+1):
        for k in range(x+1):
            if(i + j + k != n):
                res.append([i, j, k])

print(res)