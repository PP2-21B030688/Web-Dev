time = int(input())

number = cnt = 1

for i in range(time):
    if(cnt < number):
        print(number, end=" ")
        cnt += 1
    elif(cnt == number):
        print(number, end=" ")
        number += 1
        cnt = 1