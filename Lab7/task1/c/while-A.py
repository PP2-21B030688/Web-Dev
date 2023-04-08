number = int(input())

i = 1

while(i <= number):
    if( int(i**0.5) ** 2 == i ):
        print(i)
    i+=1

