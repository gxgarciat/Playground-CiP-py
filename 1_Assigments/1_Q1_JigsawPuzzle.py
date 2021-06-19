from karel.stanfordkarel import *

def main():
    """
    Write a code that makes Karel to finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
    Karel should end in the same position Karel starts in -- the bottom left corner of the world.
    """

    movetwotimes()
    pick_beeper()
    move()
    turn_left()
    movetwotimes()
    put_beeper()
    turn_left()
    turn_left()
    movetwotimes()
    rotatethreetimes()
    movetwotimes()
    move()
    turn_left()
    turn_left()


# This function makes Karel to rotate 270. 

def rotatethreetimes():
    turn_left()
    turn_left()
    turn_left()   

# This function makes Karel to rotate 180. 
def movetwotimes():
    move()
    move()



if __name__ == '__main__':
    run_karel_program('Puzzle.w')
