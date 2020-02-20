"""
Unittest to Day 03 of the Advent of Code 2019.
Title: 'Crossed Wires'
URL: https://adventofcode.com/2019/day/03
Author: tmpr
Date: 20th of February
"""

import os
import unittest

from grid import Grid


class GridTest(unittest.TestCase):

    def test_example_1(self):
        with open(os.path.join("testfiles", "example_1.in"), "r") as f:
            input_string = f.read()
        test_grid = Grid(input_string)
        self.assertEqual(
            test_grid.closest_intersection_distance(mode="manhattan"), 159)
        self.assertEqual(
            test_grid.closest_intersection_distance(mode="path_length"), 610)

    def test_example_2(self):
        with open(os.path.join("testfiles", "example_2.in"), "r") as f:
            input_string = f.read()
        test_grid = Grid(input_string)
        self.assertEqual(
            test_grid.closest_intersection_distance(mode="manhattan"), 135)
        self.assertEqual(
            test_grid.closest_intersection_distance(mode="path_length"), 410)
