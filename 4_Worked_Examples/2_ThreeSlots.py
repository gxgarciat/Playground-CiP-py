from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():

    for i in range(3):
        go_down()
        go_up()
        turn_right()
        if front_is_clear():
            move()

def go_down():
        turn_right()
        move()
        put_beeper()

def go_up():
    turn_right()
    #move()
    turn_right()
    move()



def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('Slots.w')