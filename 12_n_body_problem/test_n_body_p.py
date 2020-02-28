"""
Unittest to Day 12 of the Advent of Code 2019.
Title: 'N-Body Problem'
URL: https://adventofcode.com/2019/day/12
Author: tmpr
Date: 18th of February
"""
import pytest

from orbit import Orbit

class TestNBodyProblem:

    def test_first_example(self):
        first_example_positions = [
            [-1,  0,  2],
            [2, -10, -7],
            [4,  -8,  8],
            [3,   5, -1]
        ]
        first_orbit = Orbit(first_example_positions)
        assert first_orbit.return_orbit_energy(after_n_timesteps=10) == 179
        assert first_orbit.full_cycle_length() == 2772

    def test_second_example(self):
        second_example_positions = [
            [-8,-10,  0],
            [5,   5, 10],
            [2,  -7,  3],
            [9,  -8, -3]
        ]
        second_orbit = Orbit(second_example_positions)
        assert second_orbit.return_orbit_energy(after_n_timesteps=100) == 1940
        assert second_orbit.full_cycle_length() == 4_686_774_924