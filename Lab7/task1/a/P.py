print("First Time Moment: ")
h1 = int(input("\tHours: "))
m1 = int(input("\tMinutes: "))
s1 = int(input("\tSeconds: "))
print("Second Time Moment: ")
h2 = int(input("\tHours: "))
m2 = int(input("\tMinutes: "))
s2 = int(input("\tSeconds: "))

fullTime1 = (h1 * 3600) + (m1 * 60) + s1
fullTime2 = (h2 * 3600) + (m2 * 60) + s2

print("Second - First =", fullTime2 - fullTime1)