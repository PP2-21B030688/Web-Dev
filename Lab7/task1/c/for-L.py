binary = input()
binary = binary[::-1]

decimal = 0
power = 0

for i in binary:
    decimal += (2 ** power) * int(i) 
    power += 1

print(decimal)