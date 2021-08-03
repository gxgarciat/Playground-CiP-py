def main():

"""
Implement a program that informs the user if it is a leap year or not

"""


    year=int(input("Type the year: "))
    if year % 4 == 0:
        if year % 400 != 0:
            print("That's a leap year!")
    elif year % 400 == 0:
        print("That's a leap year!")
    else:
        print("That's not a leap year!")

if __name__ == "__main__":
    main()
