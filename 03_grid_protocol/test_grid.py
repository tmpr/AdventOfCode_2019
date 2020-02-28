"""
Unittest to Day 03 of the Advent of Code 2019.
Title: 'Crossed Wires'
URL: https://adventofcode.com/2019/day/03
Author: tmpr
Date: 20th of February
"""

import os

import pytest

from grid import Grid

if os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
    PATH = "testfiles"
else:
    PATH = os.path.join(os.path.dirname(os.path.realpath(__file__))
                        , "testfiles")

class TestGrid:

    def test_example_1(self):
        with open(os.path.join(PATH, "example_1.in"), "r") as f:
            input_string = f.read()
        test_grid = Grid(input_string)
        assert test_grid.closest_intersec_dist("manhattan") == 159
        assert test_grid.closest_intersec_dist("path_length") == 610

    def test_example_2(self):
        with open(os.path.join(PATH, "example_2.in"), "r") as f:
            input_string = f.read()
        test_grid = Grid(input_string)
        assert test_grid.closest_intersec_dist("manhattan") == 135
        assert test_grid.closest_intersec_dist("path_length") == 410
