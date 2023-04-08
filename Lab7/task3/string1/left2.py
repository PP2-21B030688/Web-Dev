def left2(s):
    firstTwo = s[:2]
    rest = s[2:len(s)]
    return rest + firstTwo

print(left2("Hello"))