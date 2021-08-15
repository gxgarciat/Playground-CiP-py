from karel.stanfordkarel import *

    """
    Write a code to make Karel to pick up a beeper from the current position if one is present
    It should not do anythin if no beepers are present).
    """

def main():


# For this repetitive task, a while loop is required.
    while beepers_present():
        pick_beeper()

if __name__ == '__main__':
    run_karel_program('SafePickup1.w')
