from karel.stanfordkarel import *


def main():
"""
Make Karel place beepers in a square (4 beepers total)
and end in the same position Karel starts in.
"""

    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    move()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
