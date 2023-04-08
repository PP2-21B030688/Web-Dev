def xyz_there(s):
    for i in range(len(s)):
        if(s[i:i+4] == ".xyz"):
            return False
        if(s[i:i+3] == "xyz"):
            return True
    return False

print(xyz_there("xyz.abc"))