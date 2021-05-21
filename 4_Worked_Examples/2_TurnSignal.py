from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
If Karel is facing a wall, put a beeper down, turn left, and move forward. If not, do nothing.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    if front_is_clear():
        put_beeper()
        turn_left()
        move()

if __name__ == "__main__":
    run_karel_program('FrontBlocked.w')