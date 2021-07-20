from karel.stanfordkarel import *

def main():

"""
File: WhileLoopWarmup.py
------------------------------
Fill the entire bottom row of the world with beepers.
"""


    while front_is_clear():
        put_beeper()
        move()
        if front_is_blocked():
            put_beeper()

if __name__ == "__main__":
    run_karel_program()
