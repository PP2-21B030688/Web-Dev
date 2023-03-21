def near_ten(n):
    if(n % 10 <= 2):
        return True
    elif(10 - n % 10 <= 2):
        return True