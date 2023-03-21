def caught_speeding(n, case):
    if(not case):
        if(n <= 60):
            return 0
        elif(n >= 61 and n <= 80):
            return 1
    else:
        if(n <= 65):
            return 0
        elif(n >= 66 and n <= 85):
            return 1
    return 2