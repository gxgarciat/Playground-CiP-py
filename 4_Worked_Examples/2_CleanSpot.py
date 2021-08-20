from karel.stanfordkarel import *

def main():

"""
Clean a spot by picking up beepers until there aren't any left.
"""


    while beepers_present():
        pick_beeper()

if __name__ == "__main__":
    run_karel_program()
