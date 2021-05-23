from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    going_up()
    # Function known as flower will be called here
    flower()
    going_down()



def going_up():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def flower():
    for i in range(3):
        put_beeper()
        move()
        turn_right()
    turn_left()
    put_beeper()

def going_down():
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()

if __name__ == "__main__":
    run_karel_program()