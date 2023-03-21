def in1to10(n, case):
    if(case):
        if(n <= 1 or n >= 10):
            return True
    else:
        if(n >= 1 and n <= 10):
            return True
    return False