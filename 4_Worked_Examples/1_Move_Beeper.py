from karel.stanfordkarel import *

def main():

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""

    move()
    pick_beeper()
    turn_left()
    movetwotimes()
    put_beeper()
    rotatethreetimes()
    move()

def movetwotimes():
        move()
        move()

def rotatethreetimes():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
