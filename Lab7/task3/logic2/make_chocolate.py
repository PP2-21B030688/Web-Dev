def make_chocolate(small, big, goal):
    if(small + big * 5 < goal): # not enough
        return -1        
    elif(small + big * 5 == goal): # exactly how many we need
        return small
    else: # more than we need
        if(big * 5 == goal): # if bigs are enough
            return 0
        elif(big * 5 < goal): # we try to use smalls, bigs are not enough
            needBig = big * 5
            needSmall = goal - needBig # in inches
            if(small >= needSmall):
                return needSmall
            return -1
        else: # too many bigs, lets use some smalls
            needBig = int((big * 5) / goal) # quantity
            needSmall = goal - needBig * 5
            if(small >= needSmall):
                return needSmall
            return -1 
        
print(make_chocolate(4, 1, 7))