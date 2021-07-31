def main():


"""
Implement a program to convert F to C

"""

    degrees_fahrenheit=float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5/9
    print(f'Temperature: {degrees_fahrenheit}F = {degrees_celsius}C')



if __name__ == "__main__":
    main()
