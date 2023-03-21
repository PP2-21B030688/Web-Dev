number = int(input())
cnt = 0

for i in range(number):
    if(int(input()) == 0):
        cnt += 1

print(cnt)