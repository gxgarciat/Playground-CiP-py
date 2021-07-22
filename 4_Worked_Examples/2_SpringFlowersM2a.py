from karel.stanfordkarel import *

def main():

"""
Karel will move until front is blocked by a wall.
"""


    
    while front_is_blocked():
        turn_left()
        move()
        turn_right()



def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
