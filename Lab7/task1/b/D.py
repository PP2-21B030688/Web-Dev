def sign(number):
    if(number > 0):
        return 1
    elif(number == 0):
        return 0
    return -1

print(sign(int(input())))