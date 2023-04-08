height = int(input("Height: "))
asc = int(input("Upperside step: "))
desc = int(input("Downside step: "))

step = asc - desc
actualDays = height - asc

days = ((int(actualDays / step)) + 1)

print(days)