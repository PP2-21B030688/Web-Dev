number = int(input())
# find 0 + -

zeros = 0
pos = 0
neg = 0

for i in range(number):
    # temp = int(input)
    if(int(input()) == 0):
        zeros += 1
    elif(int(input()) > 0):
        pos += 1
    else:
        neg += 1

print(zeros, pos, neg)