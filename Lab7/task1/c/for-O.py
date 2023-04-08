number = int(input())
hasZeros = False

for i in range(number):
    if(int(input()) == 0):
        hasZeros = True

if(hasZeros):
   print("YES")
else:
    print("NO")