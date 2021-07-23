from karel.stanfordkarel import *

def main():

"""
Karel will climb a "stem" -- Karel should start facing a wall. Karel will turn and scale the wall until there is no more wall to Karel's right.
"""

    while front_is_blocked():
        turn_left()
        move()
        turn_right()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
