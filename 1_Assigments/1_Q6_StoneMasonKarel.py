from karel.stanfordkarel import *

def main():
    """
    This function shouls make Karel do its task. 
    StoneMasonKarel should be able to solve the "repair the quad" problem from Assignment 1.
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

# This function will fill columns
def fillingcolumns():
    turn_left()

    while front_is_clear():
        if beepers_present():
            move()
        if no_beepers_present():
            put_beeper()
    if front_is_blocked():
        rotation()

# this function will make Karel cross the street
def crossstreet():
    if front_is_clear():
        for i in range(4):
            move()

# This function will make Karel rotate 90 degrees
def rotation():
    for i in range(2):
        turn_left()

# This function will make Karel go down
def goingdown():
    while front_is_clear():
        move()
    turn_left()

if __name__ == '__main__':
    run_karel_program('21x21.w')
