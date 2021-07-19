from karel.stanfordkarel import *

def main():

"""
File: ForLoopWarmup.py
------------------------------
Get Karel to do a cool backflip by turning left 4 times.
"""

    for i in range(16):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
