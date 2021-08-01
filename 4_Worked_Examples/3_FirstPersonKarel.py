def main():

"""
Implement the Karel program based on the instructions

"""


    N_COLS = 3 # notice these constants!
    N_ROWS = 3

def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    facing_direction = 'East' # this variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    curr_col = 1 # this variable ...
    curr_row = 1 # ... and this one keep track of Karel's position in the world! they may change if the user says to "move"
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    # ... more code! there's a while loop that starts on this line, but our hint ends here :^)

if __name__ == "__main__":
    main()
