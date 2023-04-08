def round10(n):
    if(n % 10 >= 5):
        return (int(n / 10) + 1) * 10 
    return n - (n % 10)

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)\
    
print(round_sum(16, 17, 18))
print(round_sum(6, 4, 4))