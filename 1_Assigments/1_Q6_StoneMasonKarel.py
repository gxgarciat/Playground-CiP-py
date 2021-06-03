from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    fillingcolumns()
    goingdown()
    crossstreet()
    fillingcolumns()
    goingdown()
    crossstreet()
    fillingcolumns()
    turn_left()
    if no_beepers_present():
        put_beeper()
        crossstreet()
    fillingcolumns()
    goingdown()
    crossstreet()
    fillingcolumns()

    goingdown()
    crossstreet()
    fillingcolumns()

    goingdown()
    crossstreet()
    fillingcolumns()

#-----Helper functions--------

def fillingcolumns():
    turn_left()

    while front_is_clear():
        if beepers_present():
            move()
        if no_beepers_present():
            put_beeper()
    if front_is_blocked():
        rotation()

def crossstreet():
    if front_is_clear():
        for i in range(4):
            move()

def rotation():
    for i in range(2):
        turn_left()

def goingdown():
    while front_is_clear():
        move()
    turn_left()

if __name__ == '__main__':
    run_karel_program('21x21.w')