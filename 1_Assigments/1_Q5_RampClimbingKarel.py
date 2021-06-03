from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        put_beeper()
        move()
        move()
        turn_left()
        move()
        rotation()
    if front_is_blocked():
        put_beeper()


def rotation():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program('RampKarel3.w')