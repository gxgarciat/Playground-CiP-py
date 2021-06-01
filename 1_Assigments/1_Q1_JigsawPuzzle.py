from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    movetwotimes()
    pick_beeper()
    move()
    turn_left()
    movetwotimes()
    put_beeper()
    turn_left()
    turn_left()
    movetwotimes()
    rotatethreetimes()
    movetwotimes()
    move()
    turn_left()
    turn_left()


def rotatethreetimes():
    turn_left()
    turn_left()
    turn_left()   

def movetwotimes():
    move()
    move()



if __name__ == '__main__':
    run_karel_program('Puzzle.w')