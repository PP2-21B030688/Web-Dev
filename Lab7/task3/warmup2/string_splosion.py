def string_splosion(s):
    cnt = 1
    res = ""
    for i in range(len(s)):
        res += s[:cnt]
        cnt += 1
    return res

print(string_splosion("abc"))