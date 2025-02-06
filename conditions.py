def OddorEven(x):
    if x % 2 == 0:
        print("x is even")
    else :
        print("x is odd")

OddorEven(3)

def PosNumber(x):
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")

PosNumber(0)

def MaxNumber(x,y,z):
    if x > y and x > z:
        print("x is the greatest")
    elif y > x and y > z:
        print("y is the greatest")
    else:
        print("z is the greatest")

MaxNumber(7,5,3)

def LeapYear(year):
    if year % 4 == 0:
        print(f"{year} is a leap year !")
    else:
        print("This is not a leap year")

LeapYear(2021)

def Operator(x,y):
    c = input("Which operation do you want to perform (A/M/S/D) : ")
    if c == "A" or "M" or "S" or "D":
        if c == "A":
            print(f"A : ",x + y)
        if c == "M":
            print(f"S : ",x * y)
        if c == "S" and x > y:
            print(f"M : ",x - y)
        if c == "D":
            print(f"D: ",x / y)
            
                
    else:
            print("Error ! Incorrect letter")


Operator(4,15)
