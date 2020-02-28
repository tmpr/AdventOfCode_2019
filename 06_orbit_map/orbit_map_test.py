"""
Unittest to Day 06 of the Advent of Code 2019.
Title: 'Universal Orbit Map'
URL: https://adventofcode.com/2019/day/06
Author: tmpr
Date: 16th of February
"""
import os

import pytest

from orbit_map import OrbitMap

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class TestOrbitMap:

    def test_small_example(self):
        with open(os.path.join("testfiles", "small_map.txt"), "r") as f:
            small_input = f.read()
        small_space_map = OrbitMap(small_input)
        assert small_space_map.count_orbits() == 42
    
    def test_small_path(self):
        with open(os.path.join("testfiles", "small_path.txt"), "r") as f:
            small_path_input = f.read()
        small_space_map = OrbitMap(small_path_input)
        assert small_space_map.find_shortest_path_length("YOU", "SAN") == 4

    def test_my_example(self):
        with open(os.path.join("testfiles", "my_map.txt"), "r") as f:
            my_input = f.read()
        my_space_map = OrbitMap(my_input)
        assert my_space_map.count_orbits() == 122782
        assert my_space_map.find_shortest_path_length("YOU", "SAN") == 271