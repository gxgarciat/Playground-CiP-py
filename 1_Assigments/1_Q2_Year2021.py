from karel.stanfordkarel import *

def main():
    """
    Write a code to make Karel to place 20 beepers, then 21 beepers.
    At the end, it should face East to the right of the 21 beepers.
    """
    
    twentybeepers()
    move()
    twentyonebeepers()
    move()

# This function makes Karel to place 20 beepers
def twentybeepers():
    for i in range(20):
        put_beeper()

# This function makes Karel to place 21 beepers
def twentyonebeepers():
    for i in range(21):
        put_beeper()

if __name__ == '__main__':
    run_karel_program('3x3.w')
