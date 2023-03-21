def front_back(s):
    last = s[:len(s)-2:-1]
    first = s[0]
    middle = s[1:len(s)-1]
    return last + middle + first

s = "1234"
s = front_back(s)
print(s)