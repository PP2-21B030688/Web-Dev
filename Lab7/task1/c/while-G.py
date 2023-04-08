x = int(input())
p = int(input())
y = int(input())

time = 0

while(x < y):
    x *= (p / 100) + 1
    time += 1

print(time)