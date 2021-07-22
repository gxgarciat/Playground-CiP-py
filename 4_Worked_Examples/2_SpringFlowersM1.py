from karel.stanfordkarel import *

def main():

"""
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""

    for i in range(3):
        put_beeper()
        move()
        turn_right()
    turn_left()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
