n = input()

if(n[len(n)-1] == "1"):
    print(n, "korova")
elif(n[len(n)-1] == "2"):
    print(n, "korovy")
else:
    print(n, "korov")