from karel.stanfordkarel import *

def main():

"""
Turn based on whether or not a beeper is present.
"""

    if beepers_present():
        turn_left()
    else:
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('1x1Beeper.w')
