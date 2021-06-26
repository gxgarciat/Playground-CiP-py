def main():

"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

    print("This program subtracts one number from another.")
    first_number=float(input("Enter first number: "))
    second_number=float(input("Enter second number: "))
    result = first_number - second_number
    print("The result is",result)

if __name__ == '__main__':
    main()
