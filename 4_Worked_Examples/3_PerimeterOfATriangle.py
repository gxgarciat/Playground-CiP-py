def main():
    
    perimeter=0
    i=1
    for i in range(1,4):
        side=float(input(f'What is the length of side {i}? '))
        perimeter=perimeter+side
    print("The perimeter of the triangle is ",perimeter)


if __name__ == "__main__":
    main()