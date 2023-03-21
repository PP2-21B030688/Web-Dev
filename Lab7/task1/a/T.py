n = input()

firstHalf = n[:int(len(n) / 2)]

forOddModifier = not(int(len(n) / 2) == (len(n) / 2)) # if even length, then 0; and vica-versa
secondHalf = n[int(len(n) / 2) + forOddModifier:len(n)][::-1]

print(int(secondHalf == firstHalf))