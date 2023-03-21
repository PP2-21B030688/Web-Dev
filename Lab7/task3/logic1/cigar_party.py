def cigar_party(n, case):
    if(case and n >= 40):
        return True
    elif(not case and n >= 40 and n <= 60):
        return True
    return False