def last2(s):
    substr = s[len(s)-2:len(s):]
    return s.count(substr) - 1 

print(last2("hixxhi"))