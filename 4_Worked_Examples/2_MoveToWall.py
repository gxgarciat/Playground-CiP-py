from karel.stanfordkarel import *

def main():


"""
Move Karel forward until you run into a wall (don't walk through the wall!).
"""



    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()
