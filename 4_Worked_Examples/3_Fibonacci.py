def main():
    
"""
Implement the Fibonacci Equation

"""

    sum = 0
    fib0= 0
    fib1= 1
    CONSTANT=10000
    print(fib0)
    print(fib1)
    while 'TRUE':
        sum  = fib1+fib0
        fib0 = fib1
        fib1 = sum
        if (fib0 < CONSTANT) and (fib1 < CONSTANT):
            print(sum)
        else:
            break

        

if __name__ == "__main__":
    main()
