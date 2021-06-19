from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    Write a code to make Karel do its task in this function. 
    Make sure to delete the 'pass' line before starting to write your own code. 
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


# This function makes Karel to rotate 270. 

def rotatethreetimes():
    turn_left()
    turn_left()
    turn_left()   

# This function makes Karel to rotate 180. 
def movetwotimes():
    move()
    move()



if __name__ == '__main__':
    run_karel_program('Puzzle.w')
