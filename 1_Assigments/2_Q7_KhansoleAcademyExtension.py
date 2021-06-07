"""
TODO: Write a description here
"""

import random 


MIN_RANDOM=10
MAX_RANDOM=99

def main():
    low=int(random.randint(MIN_RANDOM, MAX_RANDOM))
    high=int(random.randint(MIN_RANDOM, MAX_RANDOM))

    i=0
    while (i < 3):
        ans_khan=low+high
        print(f'What is {low} + {high}?')
        ans_user=int(input("Your answer: "))
        if (ans_khan == ans_user):
            i=i+1
            print(f"Correct! You've gotten {i} correct in a row.")
            if i == 3:
                print("Congratulations! You mastered addition.")
        else:
            print(f'Incorrect. The expected answer is {ans_khan}')
            i=0
        low=int(random.randint(MIN_RANDOM, MAX_RANDOM))
        high=int(random.randint(MIN_RANDOM, MAX_RANDOM))



     

if __name__ == '__main__':
    main()