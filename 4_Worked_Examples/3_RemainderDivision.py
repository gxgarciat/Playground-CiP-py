def main():
    
"""
Implement a program that divides two numbers and provides the user with the remainder 

"""

    import math

    div_1 = int(input("Please enter an integer to be divided: "))
    div_2 = int(input("Please enter an integer to divide by: "))
    res_1= div_1//div_2
    res_2 = div_1%div_2
    print(f'The result of this division is {res_1} with a remainder of {res_2}')

if __name__ == "__main__":
    main()
