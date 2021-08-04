import math

"""
Implement a program that calculates the hypotenuse, based on the Pythaorean Theorem 

"""



def main():
    ab_length = float(input("Enter the length of AB: "))
    ac_length = float(input("Enter the length of AC: "))
    bc_hypo=(ab_length**2+ac_length**2)**(0.5)
    print("The length of BC (the hypotenuse) is: ", bc_hypo)

if __name__ == "__main__":
    main()
