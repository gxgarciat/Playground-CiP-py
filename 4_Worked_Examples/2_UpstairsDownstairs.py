from karel.stanfordkarel import *

def main():
"""
Karel will climb three stair steps up and then three stair steps down.
"""
    climbing()
    descending()
        


def descending():
    for i in range(3):
        move()
        turn_threetimes()
        move()
        turn_left()

def climbing():
    for i in range(3):
        turn_left()
        move()
        turn_threetimes()
        move()

def turn_right():
    for i in range(2):
        turn_left()

def turn_threetimes():
    for i in range(3):
        turn_left()


    pass

if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')
