def main():

"""
Implement a program that informs the user if they are able to vote in Peturksbouipo, Stanlau, Mayengua

"""

    age_peturksbouipo = 16
    age_stanlau=25
    age_mayengua=48

    age=int(input("How old are you? "))
    if age >= age_mayengua:
        print("You can vote in Peturksbouipo where the voting age is 16.")
        print("You can vote in Stanlau where the voting age is 25.")
        print("You can vote in Mayengua where the voting age is 48.")
    elif age >= age_stanlau:
            print("You can vote in Peturksbouipo where the voting age is 16.")
            print("You can vote in Stanlau where the voting age is 25.")
            print("You cannot vote in Mayengua where the voting age is 48.")
    elif age >= age_peturksbouipo:
            print("You can vote in Peturksbouipo where the voting age is 16.")
            print("You cannot vote in Stanlau where the voting age is 25.")
            print("You cannot vote in Mayengua where the voting age is 48.")
    else:
            print("You cannot vote in Peturksbouipo where the voting age is 16.")
            print("You cannot vote in Stanlau where the voting age is 25.")
            print("You cannot vote in Mayengua where the voting age is 48.")

if __name__ == "__main__":
    main()
