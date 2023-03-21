def find_hypotenuse(a, b):
    return (a*a + b*b)**0.5

a = int(input("Catet1 ? "))
b = int(input("Catet2 ? "))

print("Hypotenuse is ", find_hypotenuse(a, b))