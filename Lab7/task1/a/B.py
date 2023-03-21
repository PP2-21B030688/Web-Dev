def is_in_range(number):
    if( (number > 0 and number <= 10000 ) or ( number < 0 and number >= -10000 ) ):
        return True
    return False

number = int( input("Input your number! ") )

def main():
    if( not is_in_range(number) ):
        print("Module of the number should not exceed 10000")
        return
    
    print("The next number for the number", number, "is", number + 1)
    print("The previous number for the number", number, "is", number - 1)

main()