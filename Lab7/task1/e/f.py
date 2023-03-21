def getPower(n, pow, cnt, mult):
    if(cnt == abs(pow)):
        return n
    if(pow > 0):
        return getPower(n * mult, pow, cnt + 1, mult)
    elif(pow == 0):
        return 1
    else:
        return getPower(1 / (n * mult), pow, cnt + 1, mult)

n = int(input())
pow = int(input())

print(getPower(n, pow, 1, n))