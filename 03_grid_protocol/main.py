"""
Solution to Day 03 of the Advent of Code 2019.
Title: 'Crossed Wires'
URL: https://adventofcode.com/2019/day/03
Author: tmpr
Date: 20th of February
"""

from grid import Grid

def main():
    with open("grid_instruction.in") as file:
        my_input = file.read()
    my_grid = Grid(my_input)
    print(my_grid.closest_intersection_distance(mode="manhattan"))
    print(my_grid.closest_intersection_distance(mode="path_length"))


if __name__ == "__main__":
    main()
