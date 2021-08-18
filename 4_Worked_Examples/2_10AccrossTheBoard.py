from karel.stanfordkarel import *

def main():

"""

Place 10 beepers in all spots on the bottom row of any sized world.
"""

    while front_is_clear(): #front_is_clear():
        tenbeepers()
        move()
    tenbeepers()
    
            
def tenbeepers():
    for i in range(10):
        put_beeper()

if __name__ == "__main__":
    run_karel_program('TensKarel3.w')
