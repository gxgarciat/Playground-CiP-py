def main():
"""
Places a zig zag pattern of beepers in the world.
"""

    while front_is_clear():
        put_beeper()
        top_beepers()
        turn_right()
        move()
        turn_left()
        if front_is_blocked():
            pass
        else: 
            move()

def top_beepers():
    move()
    turn_left()
    move()
    put_beeper()

def turn_right():
    for i in range(2):
        turn_left()

def turn_threetimes():
    for i in range(3):
        turn_left()

    pass

if __name__ == "__main__":
    run_karel_program('ZigZag2.w')
