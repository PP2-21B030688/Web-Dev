x = input()

beginningZeros = True
for i in x:
    if(i == "0"):
        if(not beginningZeros):
            print(i, end="")
    else:
        print(i, end="")
        beginningZeros = False

if(beginningZeros):
    print("0")