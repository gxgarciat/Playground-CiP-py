def main():

"""
Implement a program that provides a wholesome phrase

""" 

    motivation="I am capable of doing anything I put my mind to."
    text=input("Please type the following affirmation: I am capable of doing anything I put my mind to.")
    while motivation != text:
        print("That was not the affirmation.")
        print("")
        text=input("Please type the following affirmation: I am capable of doing anything I put my mind to.")
    print("That's right! :)")

if __name__ == "__main__":
    main()
