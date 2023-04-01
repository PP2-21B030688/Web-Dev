k = int(input())

if(k < 3):
    print("NO")
else:
    if(k == 3 or k == 5):
        print("YES")
    else:
        acquire = k % 5
        if(acquire == 0):
            print("YES")
        elif(acquire < 3 or acquire == 4):
            print("NO")
        else:
            print("YES")
