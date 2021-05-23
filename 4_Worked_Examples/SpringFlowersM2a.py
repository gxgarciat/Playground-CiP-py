from karel.stanfordkarel import *

"""
File: MoveToWall.py
------------------------------
Karel will move until front is blocked by a wall.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    
    while front_is_blocked():
        turn_left()
        move()
        turn_right()



def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()