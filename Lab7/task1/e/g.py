def getPosPower(n, pow):
    if(pow == 1):
        return n
    if (pow % 2 == 0):
        return getPosPower(n * n, pow / 2)
    else:
        return n * getPosPower(n * n, int(pow / 2))
    
def getNegPower(n, pow):
    if(pow == 1):
        return n
    if (pow % 2 == 0):
        return getPosPower(1 / (n * n), pow / 2)
    else:
        return 1 / (n * getPosPower(n * n, int(pow / 2)))

n = int(input())
pow = int(input())

if(pow == 0):
    print(1)
elif(pow > 0):
    print(getPosPower(n, pow))
else:
    print(getNegPower(n, pow*-1))


"""
3, 3

1: return 27, 2
2: 

"""