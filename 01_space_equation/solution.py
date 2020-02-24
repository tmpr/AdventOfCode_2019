"""
Solution to Day 01 of the Advent of Code 2019.
Title: 'The Tyranny of the Rocket Equation'
URL: https://adventofcode.com/2019/day/01
Author: tmpr
Date: 24th of February
"""

from math import floor

def fuel_cost(mass: int, recursive=False) -> int:
    """
    Given some mass, calulates its fuel cost. \n
    If `recursive=True`, recursively returns the
    sum of the fuel costs of the fuel needed.
    """
    if recursive:
        needed_fuel = floor(mass/3) - 2
        if needed_fuel <= 0:
            return 0
        else:
            return (needed_fuel + 
                   fuel_cost(needed_fuel, recursive=True))
    else:
        return floor(mass/3) - 2

def main():
    with open("my_input.in", "r") as f:
        module_string = f.read()
    module_masses = module_string.splitlines()
    
    fuel_needed = sum((fuel_cost(int(mass)) for mass 
                       in module_masses))
    rec_fuel_needed = sum((fuel_cost(int(mass), recursive=True) 
                           for mass in module_masses))
                           
    print("Fuel needed not including cost of the fuel itself:")
    print(fuel_needed)
    print("Fuel needed including the fuel cost of the fuel:")
    print(rec_fuel_needed)

if __name__ == "__main__":
    main()