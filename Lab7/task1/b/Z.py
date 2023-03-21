n = int(input())

# one -> 15rub;  5 -> 70rub;  10 -> 125 rub;  20 -> 230rub;  60 -> 440rub

one, five, ten, twenty, sixty = 0, 0, 0, 0, 0

sixty = int(n / 60) # 2
remaining = n % 60 # 9

if(int(remaining / 20) != 0):
    twenty = int(remaining / 20)
    remaining = remaining % 20
else: # 0 -> 19
    if(remaining <= 17): # pay with one, five and ten
        if(remaining >= 10):
            ten += int(remaining / 10)
            remaining %= 10
        else: # 0 -> 9
            if(remaining >= 5):
                five += int(remaining / 5)
                remaining %= 5
            else: # 0 -> 4
                one += remaining
                remaining = 0
    else: # use twenty
        twenty += 1
        remaining = 0

if(remaining):
    if(remaining <= 17): # pay with one, five and ten
        if(remaining >= 10):
            ten += int(remaining / 10)
            remaining %= 10
        else: # 0 -> 9
            if(remaining >= 5):
                five += int(remaining / 5)
                remaining %= 5
            else: # 0 -> 4
                one += remaining
    else: # use twenty
        twenty += 1
        remaining = 0

print(one, five, ten, twenty, sixty)