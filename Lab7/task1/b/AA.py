m = int(input())
n = int(input())
x = int(input())
y = int(input())

up, down, right, left = 0, 0, 0, 0

if(y + 1 <= n):
    up = y + 1
if(y - 1 >= 1):
    down = y - 1
if(x + 1 <= m):
    right = x + 1
if(x - 1 >= 1):
    left = x - 1

coords = [up, down, right, left]

if(up):
    print(x, up)
if(right):
    print(right, y)
if(down):
    print(x, down)
if(left):
    print(left, y)
