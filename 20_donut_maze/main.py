"""
Solution to Day 20 of the Advent of Code 2019.
Title: 'Space Stoicometry'
URL: https://adventofcode.com/2019/day/20
Author: tmpr
Date: 21th of February
"""

import os

from portal_maze import PortalMaze
from recursive_maze import RecursiveMaze


def main():
    with open(os.path.join("inputs", "my_input.in"), "r") as f:
        example_input = f.read()
    simple_maze = PortalMaze(example_input)
    print("Shortest path length of the simple maze: ",
          simple_maze.shortest_path_length)
    recursive_maze = RecursiveMaze(example_input, depth=50)
    print("Shortest path length of the multidimensional, recursive maze: ",
          recursive_maze.shortest_path_length)


if __name__ == "__main__":
    main()
