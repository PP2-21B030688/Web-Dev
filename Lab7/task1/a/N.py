def calculateBreaksTime(lesson, breaksTime = 0):
    if(lesson <= 0):
        return breaksTime       # base case
    if(lesson % 2 == 0):
        return calculateBreaksTime(lesson - 1, breaksTime + 15)
    else:
        return calculateBreaksTime(lesson - 1, breaksTime + 5)
    


lesson = int(input("Lesson number? "))

breaksTime = calculateBreaksTime(lesson - 1)
fullTime = breaksTime + lesson * 45

hours = int(fullTime / 60);

print(hours + 9, fullTime - ( hours * 60 ) ) 