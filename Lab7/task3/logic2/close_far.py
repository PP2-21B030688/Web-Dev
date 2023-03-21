def close_far(a, b, c):
    if(abs(b - a) <= 1 and abs(c - a) > 1 and abs(c - b) > 1):
        return True
    elif(abs(c - a) <= 1 and abs(b - a) > 1 and abs(b - c) > 1):
        return True
    return False

print(close_far(4, 1, 3))