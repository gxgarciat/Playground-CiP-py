from karel.stanfordkarel import *

def main():
    """
    Karel will move up and over the archway.
    """
    turn_left()
    movethreetimes()
    rotation()
    movethreetimes()
    rotation()
    movethreetimes()

def movethreetimes():
    for i in range(3):
        move()

def rotation():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
