from karel.stanfordkarel import *


def main():

"""
Put 4 beepers down in a row, starting with Karel's current position.
"""

    while front_is_clear():
        put_beeper()
        move()

if __name__ == "__main__":
    run_karel_program()
