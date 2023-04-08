def make_bricks(small, big, goal):
    if(small + big * 5 < goal): # not enough
        return False        
    elif(small + big * 5 == goal): # exactly how many we need
        return True
    else: # more than we need
        if(big * 5 == goal): # if bigs are enough
            return True
        elif(big * 5 < goal): # we try to use smalls, bigs are not enough
            needBig = big * 5
            needSmall = goal - needBig # in inches
            if(small >= needSmall):
                return True
            return False
        else: # too many bigs, lets use some smalls
            needBig = int((big * 5) / goal) # quantity
            needSmall = goal - needBig * 5
            if(small >= needSmall):
                return True
            return False 
        
print(make_bricks(3, 2, 10))