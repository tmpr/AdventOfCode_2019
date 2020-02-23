"""
Solution to Day 24 of the Advent of Code 2019.
Title: 'Planet of Discord'
URL: https://adventofcode.com/2019/day/24
Author: tmpr
Date: 23th of February
"""

import os

from bug_field import BugField
from recursive_bug_field import RecursiveBugField
from functions import calculate_biodiversity

def main():
    with open(os.path.join("inputs", "my_input.in"), "r") as f:
        my_input_string = f.read()
    
    my_bug_field = BugField(my_input_string)
    
    rec_bug_field = RecursiveBugField(my_input_string, max_recursion_depth=310)
    rec_bug_field.forward(minutes = 200)

    print("Answer 1: ")
    print(calculate_biodiversity(my_bug_field.first_rec_state))
    print("Answer 2: ")
    print(rec_bug_field.total_bugs())

if __name__ == "__main__":
    main()