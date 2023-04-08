n = int(input())

# 60 -> 440rub; 10 -> 125rub; 1 -> 15rub
# 129

one, ten, sixty = 0, 0, 0

sixty = int(n / 60) # 2
remaining = n % 60 # 9
print(remaining)

if(int(remaining / 10) != 0):
    ten = int(remaining / 10)
    remaining = remaining % 10
else:
    if(remaining * 15 > 125):
        ten += 1
    else:
        one = remaining

print(one, ten, sixty)