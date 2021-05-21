from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Invert the spot Karel is currently standing on.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == "__main__":
    run_karel_program('InvertBeeper.w')