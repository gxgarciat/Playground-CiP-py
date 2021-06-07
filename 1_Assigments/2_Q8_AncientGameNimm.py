"""
TODO: Write a description here
"""

import random

def main():
    stones_left=20
    while (stones_left > 0):
        print(f'There are {stones_left} stones left')
        removed=int(input(f'Player 1 would you like to remove 1 or 2 stones? '))
        while (removed != 1) and (removed != 2):
            removed = int(input("Please enter 1 or 2: "))
        stones_left=stones_left-removed
        print("")
        
        if (stones_left < 0):
            print("Game over")
            break
        elif (stones_left == 0):
                print("Player 2 wins!")
                break

        print(f'There are {stones_left} stones left')
        removed=int(input(f'Player 2 would you like to remove 1 or 2 stones? '))
        while (removed != 1) and (removed != 2):
            removed = int(input("Please enter 1 or 2: "))
        stones_left=stones_left-removed
        print("")

        if (stones_left < 0):
            print("Game over")
            break
        elif (stones_left == 0):
                print("Player 1 wins!")
                break


if __name__ == '__main__':
    main()