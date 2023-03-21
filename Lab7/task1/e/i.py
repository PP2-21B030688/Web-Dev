def getFactorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def getCnK(n, k):
    upper = getFactorial(n)
    lower = getFactorial(k) * getFactorial(n-k)
    return int(upper / lower)

n = int(input())
k = int(input())

print(getCnK(n, k))