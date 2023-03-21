pupils = int(input("How many pupils? ")) # 7
apples = int(input("How many apples? ")) # 30

remainder = apples % pupils # 2

print((pupils - remainder) * (remainder / (remainder + 1) ).__ceil__() )