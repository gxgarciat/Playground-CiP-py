from karel.stanfordkarel import *


def main():

"""
File: IfElseWarmup.py
------------------------------
Invert the spot Karel is currently standing on.
"""

    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == "__main__":
    run_karel_program('InvertBeeper.w')
