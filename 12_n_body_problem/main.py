"""
Solution to Day 12 of the Advent of Code 2019.
Title: 'N-Body Problem'
URL: https://adventofcode.com/2019/day/12
Author: tmpr
Date: 18th of February
"""

from orbit import Orbit


def main():
    my_starting_positions = [
        [-10, -13, 7],
        [1, 2, 1],
        [-15, -3, 13],
        [3, 7, -4]
    ]
    my_orbit = Orbit(my_starting_positions)
    print("Orbit-energy after 1000 timesteps:\n",
          my_orbit.return_orbit_energy(after_n_timesteps=1000))
    print("Time it takes the Orbit to return to its initial state:\n",
          my_orbit.full_cycle_length())


if __name__ == "__main__":
    main()