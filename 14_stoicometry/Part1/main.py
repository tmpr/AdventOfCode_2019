"""
Solution to Day 14 of the Advent of Code 2019.
Title: 'Space Stoicometry'
URL: https://adventofcode.com/2019/day/14
Author: tmpr
Date: 16th of February
"""
import os
from math import ceil

from functions_stoic import compute_ore_cost

def main():
    with open(os.path.join("example_files", "my_input.txt"), "r") as f:
        my_input = f.read()
    print(compute_ore_cost(my_input))

if __name__ == "__main__":
    main()
    
