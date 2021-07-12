import random 

   """
   Prints out a randomly generated addition problem
   and checks if the user answers correctly.
   """

MIN_RANDOM=10
MAX_RANDOM=99

def main():
    low=int(random.randint(MIN_RANDOM, MAX_RANDOM))
    high=int(random.randint(MIN_RANDOM, MAX_RANDOM))
    ans_khan=low+high
    print(f'What is {low} + {high}?')
    ans_user=int(input("Your answer: "))
    if (ans_khan == ans_user):
        print("Correct!")
    else:
        print(f'Incorrect. The expected answer is {ans_khan}')

     
if __name__ == '__main__':
    main()
