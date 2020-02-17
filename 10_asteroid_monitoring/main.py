"""
Solution to Day 10 of the Advent of Code 2019.
Title: 'Universal Orbit Map'
URL: https://adventofcode.com/2019/day/10
Author: tmpr
Date: 17th of February
"""
from asteroid_belt import AsteroidBelt

def main():
    with open("my_example.txt", "r") as f:
        my_example_field = f.read()
    belt = AsteroidBelt(my_example_field)
    print("Initialized asteroid-belt and found best asteroid.")
    print(belt.best_asteroid.simulate_destruction(n_asteroids=200,
                                    v_title="my_destruction",
                                    make_video=True))

if __name__ == "__main__":
    main()
