def end_other(a, b):
    if(len(a) >= len(b)):
        short = b.lower()
        long = a.lower()
    else:
        long = b.lower()
        short = a.lower()
    if(long[:len(long)-len(short)-1:-1][::-1] == short):
        return True
    return False

print(end_other("HiAbC", "abC"))  