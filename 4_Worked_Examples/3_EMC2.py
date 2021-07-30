def main():
"""
Implement the Equation for the mass-energy equivalence

"""

    
    C = 299792458
    m = float(input("Enter kilos of mass: "))
    print("e = m * C^2...")
    print(f'm = {m} kg')
    print(f'C = {C} m/s')
    e=m*C**2 
    print(f'{e} joules of energy!')
    

if __name__ == "__main__":
    main()
