from karel.stanfordkarel import *

def main():

"""
If Karel is facing a wall, put a beeper down, turn left, and move forward. If not, do nothing.
"""


    if front_is_clear():
        put_beeper()
        turn_left()
        move()

if __name__ == "__main__":
    run_karel_program('FrontBlocked.w')
