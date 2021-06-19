from karel.stanfordkarel import *

def main():
    """
    Write a code, RampClimbingKarel, to draw a line with slope 1/2 in 
    any odd sized world.
    """

# This while-loop will keep Karel moving until it reaches a wall
    while front_is_clear():
        put_beeper()
        move()
        move()
        turn_left()
        move()
        rotation()
    if front_is_blocked():
        put_beeper()

# This function makes Karel rotate 270 degrees.
def rotation():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program('RampKarel3.w')
