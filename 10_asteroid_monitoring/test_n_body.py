"""
Unittest to Day 10 of the Advent of Code 2019.
Title: 'Universal Orbit Map'
URL: https://adventofcode.com/2019/day/10
Author: tmpr
Date: 17th of February
"""

import os
import pytest

from asteroid_belt import AsteroidBelt

if os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
    RP = ""
else:
    RP = os.path.dirname(os.path.realpath(__file__))


class TestAsteroidBeltExamples:

    def test_small_example(self):
        with open(os.path.join(RP, "testfiles", "small_example.txt"), "r") as f:
            input_field = f.read()
        belt = AsteroidBelt(input_field)
        assert belt.best_asteroid.visible_asteroid_count == 8
        assert belt.best_asteroid.coordinates == (3, 4)

    def test_medium_example1(self):
        with open(os.path.join(RP, "testfiles", "medium_example1.txt"), "r") as f:
            input_field=f.read()
        belt=AsteroidBelt(input_field)
        assert belt.best_asteroid.visible_asteroid_count == 33
        assert belt.best_asteroid.coordinates == (5, 8)

    def test_medium_example2(self):
        with open(os.path.join(RP, "testfiles", "medium_example2.txt"), "r") as f:
            input_field=f.read()
        belt=AsteroidBelt(input_field)
        assert belt.best_asteroid.visible_asteroid_count == 35
        assert belt.best_asteroid.coordinates == (1, 2)

    def test_medium_example3(self):
        with open(os.path.join(RP, "testfiles", "medium_example3.txt"), "r") as f:
            input_field=f.read()
        belt=AsteroidBelt(input_field)
        assert belt.best_asteroid.visible_asteroid_count == 41
        assert belt.best_asteroid.coordinates == (6, 3)


    def test_large_example(self):
        with open(os.path.join(RP, "testfiles", "large_example.txt"), "r") as f:
            input_field=f.read()
        belt=AsteroidBelt(input_field)
        assert belt.best_asteroid.visible_asteroid_count == 210
        assert belt.best_asteroid.coordinates == (11, 13)
        assert belt.best_asteroid.simulate_destruction(200, False) == 802
