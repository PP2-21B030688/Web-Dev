# speed = int(input("The speed: "))
# stop = int(input("After how many hours should a car stop? "))

speed = int(input())
stop = int(input())

if(stop > 0):
    if(speed >= 0):
        if(speed * stop >= 109):
            print( (speed * stop) % 109 )
        else:
            print(speed * stop)
    else:
        if( (speed * stop * -1) > 109):
            print( (speed * stop * -1) % 109 )
        else:
            print( 109 - (speed * stop * -1) )
else:
    print(0)
