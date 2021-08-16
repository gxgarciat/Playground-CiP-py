from karel.stanfordkarel import *

def main():

"""
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to

instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


    rotation()
    move()
    turn_left()
    movethreepositions()
    pick_beeper()
    turn_left()
    turn_left()
    movethreepositions()
    rotation()
    move()
    rotation()

def rotation():
    for i in range(3):
        turn_left()

def movethreepositions():
    for i in range(3):
        move()

if __name__ == "__main__":
    run_karel_program()
