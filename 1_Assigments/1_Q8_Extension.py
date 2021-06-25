from karel.stanfordkarel import *

def main():
    """
    
    """
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
    
    if front_is_blocked():
        put_beeper()



if __name__ == "__main__":
    run_karel_program()
