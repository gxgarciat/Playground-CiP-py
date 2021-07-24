from karel.stanfordkarel import *

def main():


"""

Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
"""



    while front_is_clear():
        move()

    going_up()
    # Function known as flower will be called here
    flower()
    going_down()

    while front_is_clear():
        move()
    
    going_up()
    flower()
    going_down()

    while front_is_clear():
        move()



def going_up():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def flower():
    for i in range(3):
        put_beeper()
        move()
        turn_right()
    turn_left()
    put_beeper()

def going_down():
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()

if __name__ == "__main__":
    run_karel_program('SpringFlowers1.w')
