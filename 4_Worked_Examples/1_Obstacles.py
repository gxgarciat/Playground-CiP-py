from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    obstacles()
    obstacles()
    obstacles()
    move()
    move()

def obstacles():
    turn_left()
    move()
    rotation()
    move()
    rotation()
    move()
    put_beeper()
    turn_left()

def rotation():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
