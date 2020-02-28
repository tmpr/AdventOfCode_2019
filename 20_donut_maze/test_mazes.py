"""
Unittest to Day 20 of the Advent of Code 2019.
Title: 'Donut Maze'
URL: https://adventofcode.com/2019/day/20
Author: tmpr
Date: 21th of February
"""

import pytest
import os
import networkx as nx

from portal_maze import PortalMaze
from recursive_maze import RecursiveMaze

if os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
    PATH = "inputs"
else:
    PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                      "inputs")

class TestPortalMaze:

    def test_example_1(self):
        with open(os.path.join(PATH, "example_1.in"), "r") as f:
            example_input = f.read()
        example_maze = PortalMaze(example_input)
        recursive_maze = RecursiveMaze(example_input, depth=20)

        assert example_maze.shortest_path_length == 23
        assert recursive_maze.shortest_path_length == 26
        
    def test_example_2(self):
        with open(os.path.join(PATH, "example_2.in"), "r") as f:
            example_input = f.read()
        example_maze = PortalMaze(example_input)
        recursive_maze = RecursiveMaze(example_input, depth=100)

        assert example_maze.shortest_path_length == 58
        assert recursive_maze.shortest_path_length == None

    def test_recursive_example(self):
        with open(os.path.join(PATH, "example_3.in"), "r") as f:
            example_input = f.read()
        recursive_maze = RecursiveMaze(example_input, depth=50)
        assert recursive_maze.shortest_path_length == 396
