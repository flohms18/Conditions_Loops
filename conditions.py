def OddOrEven(x):
    if x % 2 == 0:
        print("x is even !")
    else:
        print("x is odd !")

OddOrEven(4)

def IsPositive(x):
    if x > 0:
        print("x is positive !")
    else:
        print("x is negative !")

IsPositive(-4)

def GreatestNumber(x,y,z):
    if x > y and x > z:
        print("x is the greatest number !")
    elif y > x and y > z:
        print("y is the greatest number !")
    else:
        print("z is the greatest number !")

GreatestNumber(4,5,6)

def IsLeapYear(year):
    if year % 4 == 0:
        print("This is a leap year !")
    else:
        print("This is not a leap year !")

IsLeapYear(2020)

def IsPrimeNumber(x):
    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                print("This is not a prime number !")
                break
        else:
            print("This is a prime number !")
    else:
        print("This is not a prime number !")

