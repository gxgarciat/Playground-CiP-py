from karel.stanfordkarel import *

def main():

"""
Turn left until Karel is facing a wall.
"""


    while front_is_clear():
        turn_left()


if __name__ == "__main__":
    run_karel_program()
