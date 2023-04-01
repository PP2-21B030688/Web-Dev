def string_bits(s):
    res = ""
    for i in range(0,len(s),2):
        res += s[i]
    return res

print(string_bits('Hello'))