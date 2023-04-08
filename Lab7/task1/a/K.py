time = int(input("Time passed: "))

print(int(time / 60) % 24, end=" ")
print(time - int(time / 60)*60)