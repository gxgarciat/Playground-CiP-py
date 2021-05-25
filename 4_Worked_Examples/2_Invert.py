from karel.stanfordkarel import *

"""
File: InvertKarel.py
-----------------------
Inverts the pattern of beepers in a single row world.
"""

def main():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            move()
        else:
            put_beeper()
            move()
    if no_beepers_present():
        put_beeper()
    else: 
        pick_beeper()
    
    
    pass

if __name__ == "__main__":
    run_karel_program('Invert1.w')