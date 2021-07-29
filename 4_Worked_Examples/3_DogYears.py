def main():

   
"""
Write a program that asks the user their age in human years
Then, the program will calculate the age in dog years

"""
    
    age_human=float(input("Enter an age in human years: "))
    age_dog=age_human*7.18
    print(f"That's {age_dog} in dog years!")

if __name__ == "__main__":
    main()
