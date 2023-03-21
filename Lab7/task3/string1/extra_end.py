def extra_end(s):
    last = s[len(s)-2:len(s)]
    return last * 3

print(extra_end("Hello"))