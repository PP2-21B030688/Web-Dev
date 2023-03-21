def getMostFrequent(a, b, c):
    if(a == b or a == c):
        return a
    elif(b == c):
        return b
    
a = int(input())
b = int(input())
c = int(input())

print(getMostFrequent(a, b, c))