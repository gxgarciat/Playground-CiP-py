import random

def main():

    #specific range
    min = 0
    max = 0.7

    #generate a random floating point number
    heads = min + (max-min)*random.random()

    print(f'The probability of heads is {heads}')

if __name__ == "__main__":
    main()