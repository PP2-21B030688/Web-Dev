n = int(input())

students = {}

for i in range(n):
    inputRow = input().split()
    students[inputRow[0]] = [inputRow[1], inputRow[2], inputRow[3]]

name = input()

sum = 0

for i in students[name]:
    sum += int(i)

print(sum / 3)