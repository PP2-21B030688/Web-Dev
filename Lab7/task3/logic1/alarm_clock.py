def alarm_clock(n, case):
    if(case):
        if(n == 6 or n == 7):
            print("off")
        else:
            print("10:00")
    else:
        if(n == 6 or n == 7):
            print("10:00")
        else:
            print("7:00")