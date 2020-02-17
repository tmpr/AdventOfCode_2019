"""
Unittest to Day 06 of the Advent of Code 2019.
Title: 'Universal Orbit Map'
URL: https://adventofcode.com/2019/day/06
Author: tmpr
Date: 16th of February
"""
import unittest
import os

from orbit_map import OrbitMap

class SpaceMapTests(unittest.TestCase):

    def test_small_example(self):
        with open(os.path.join("testfiles", "small_map.txt"), "r") as f:
            small_input = f.read()
        small_space_map = OrbitMap(small_input)
        self.assertEqual(small_space_map.count_orbits(), 42)
    
    def test_small_path(self):
        with open(os.path.join("testfiles", "small_path.txt"), "r") as f:
            small_path_input = f.read()
        small_space_map = OrbitMap(small_path_input)
        self.assertEqual(small_space_map.find_shortest_path_length("YOU", "SAN"), 4)

    def test_my_example(self):
        with open(os.path.join("testfiles", "my_map.txt"), "r") as f:
            my_input = f.read()
        my_space_map = OrbitMap(my_input)
        self.assertEqual(my_space_map.count_orbits(), 122782)
        self.assertEqual(my_space_map.find_shortest_path_length("YOU", "SAN"), 271)