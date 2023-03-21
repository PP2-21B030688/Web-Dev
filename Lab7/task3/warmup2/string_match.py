def string_match(a, b):
    small = (a if len(a) >= len(b) else b)
    cnt = 0
    for i in range(len(small)):
        if(a[i] == b[i]):
            cnt += 1
    return cnt

print(string_match("abc", "abc"))