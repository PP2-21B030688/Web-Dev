number = input()
answer = input()
isSymmetrical = False

if(len(number)>=4):
    if(len(number) % 2 == 0 ):
        if(number[:int(len(number) / 2)] == number[int( len(number) / 2 ):int(len(number))]):
            isSymmetrical = True
    else:
        if(number[:int(len(number)/2)] == number[int(len(number)/2 + 1):int(len(number))]):
            isSymmetrical = True
if(not isSymmetrical and answer!="1"):
    print("YES")
else:
    print("NO")