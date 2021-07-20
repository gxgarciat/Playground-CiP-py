from karel.stanfordkarel import *

def main():

"""
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""


    for i in range(4):
        move_forward()
        beeperstatus()
        turn_right()
        move_forward()
        if front_is_blocked():
            turn_threetimes()
        move()
        turn_threetimes()
    move_forward()
    beeperstatus()
    turn_right()
    move_forward()
    turn_right()


            
    
def move_forward():
    while front_is_clear():
        move()

def beeperstatus():
    if no_beepers_present():
        put_beeper()
    
    
def turn_right():
    for i in range(2):
        turn_left()

def turn_threetimes():
    for i in range(3):
        turn_left()


    
    



if __name__ == "__main__":
    run_karel_program()
