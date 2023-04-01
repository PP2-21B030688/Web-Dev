def missing_char(s, n):
    res = ""
    for i in range(len(s)):
        if(i != n):
            res += s[i]
    return res

s = input()
n = int(input())

s = missing_char(s, n)
print(s)