def isEven(n):
    return (True if n % 2 == 0 else False)

a = int(input())
b = int(input())
c = int(input())

checkA = isEven(a)
checkB = isEven(b)
checkC = isEven(c)

if((checkA or checkB or checkC) and not(checkA and checkB and checkC)):
    print("YES")
else:
    print("NO")