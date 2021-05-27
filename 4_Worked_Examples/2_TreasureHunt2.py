from karel.stanfordkarel import *

"""
File: TreasureHunt2.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def main():

    while front_is_clear():
        move()
        if beepers_present():
            while beepers_present():
                pick_beeper()
            turn_left()
        if front_is_blocked():
            turn_right()

def turn_right():
    for i in range(2):
        turn_left()

    pass

if __name__ == "__main__":
    run_karel_program()