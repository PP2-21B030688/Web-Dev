number = input("Three-Digit Number? ")
sum = 0

for i in range(len(number)):
    sum += int(number[i])

print("Sum of digits is", sum)