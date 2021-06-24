from karel.stanfordkarel import *

	
def main():

	"""
	This program should place a beeper on the middle of the first row.
	"""

    while no_beepers_present():
        build_wall()
    if left_is_blocked():
        turn_left()
        back_to_start()
        deconstruct_wall()
        turn_left()
        place_last_beeper()
    else:
        back_to_start()
        while beepers_present():
            deconstruct_wall()
        place_last_beeper()

# Helper functions

# This function build a wall
def build_wall():
    while no_beepers_present():
        if front_is_clear():
            put_beeper()
            move()
        else:
            put_beeper()
            turn_left()
            if front_is_clear():
                move()
    if left_is_clear():
        turn_left()
        move()
        turn_left()
        move()
        turn_right()

# This function deconstruct the wall
def deconstruct_wall():
    while beepers_present():
        if front_is_clear():
            pick_beeper()
            move()
        else:
            pick_beeper()
            turn_left()
            if front_is_clear():
                move()
    if left_is_clear():
        turn_left()
        move()
        turn_left()
        move()
        turn_right()

def back_to_start():
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

# This function will place beepers
def place_last_beeper():
    if facing_north():
        turn_left()
        turn_left()
    if facing_east():
        turn_right()
    if facing_west():
        turn_left()
    while front_is_clear():
        move()
    put_beeper()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()
    

if __name__ == '__main__':
    run_karel_program('Midpoint2.w')
