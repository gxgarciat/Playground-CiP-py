from karel.stanfordkarel import *

def main():
    """
    Write a code where CleanupKarel should be able to pick up all beepers 
    from the first row of any sized world and end in the bottom right corner facing East.
    """

# This code comprises a while-loop and a conditional, to check if beepers are present.
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
