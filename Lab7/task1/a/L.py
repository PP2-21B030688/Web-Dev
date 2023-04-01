def formatTime(time):
    if(time <= 9):
        return "0" + str(time)
    return time    

time = int(input("Seconds passed: "))

time

hours = int(time / 3600)
minutes = int ( (time - hours * 3600) / 60 )

print(hours % 24, end=":")
print(formatTime(minutes), end=":")
print( formatTime(time - ( hours * 3600 + minutes * 60 )) )
