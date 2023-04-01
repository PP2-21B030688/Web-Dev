def convertThousands(n):
    if(n == 9):
        return "<IXM>"
    elif(n == 8):
        return "<VIIIM>"
    elif(n == 7):
        return "<VIIM>"
    elif(n == 6):
        return "<VIM>"
    elif(n == 5):
        return "<VM>"
    elif(n == 4):
        return "<IVM>"
    elif(n == 3):
        return "<IIIM>"
    elif(n == 2):
        return "<IIM>"
    elif(n == 1):
        return "<IM>"

def convertHundreds(n):
    if(n == 9):
        return "<IXC>"
    elif(n == 8):
        return "<DIIIC>"
    elif(n == 7):
        return "<DIIC>"
    elif(n == 6):
        return "<DC>"
    elif(n == 5):
        return "D"
    elif(n == 4):
        return "<IVC>"
    elif(n == 3):
        return "<IIIC>"
    elif(n == 2):
        return "<IIC>"
    elif(n == 1):
        return "C"

def convertDozens(n):
    if(n == 9):
        return "<IXX>"
    elif(n == 8):
        return "<VIIIX>"
    elif(n == 7):
        return "<VIIX>"
    elif(n == 6):
        return "<VIX>"
    elif(n == 5):
        return "<VX>"
    elif(n == 4):
        return "<IVX>"
    elif(n == 3):
        return "<IIIX>"
    elif(n == 2):
        return "<IIX>"
    elif(n == 1):
        return "<IX>"

def convertOnes(n):
    if(n == 9):
        return "IX"
    elif(n == 8):
        return "VIII"
    elif(n == 7):
        return "VII"
    elif(n == 6):
        return "VI"
    elif(n == 5):
        return "V"
    elif(n == 4):
        return "IV"
    elif(n == 3):
        return "III"
    elif(n == 2):
        return "II"
    elif(n == 1):
        return "I"
    

n = int(input())

thousands = int(n / 1000)
n %= 1000

hundrends = int(n / 100)
n %= 100

dozens = int(n / 10)
n %= 10

romanThousands = convertThousands(thousands)
romanHundreds = convertHundreds(hundrends)
romanDozens = convertDozens(dozens)
romanOnes = convertOnes(n)
