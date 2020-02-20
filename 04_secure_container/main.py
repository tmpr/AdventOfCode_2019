"""
Solution to Day 04 of the Advent of Code 2019.
Title: 'Secure Container'
URL: https://adventofcode.com/2019/day/04
Author: tmpr
Date: 20th of February
"""

from functions import possible_elve_passwords


def main():
    my_range = range(168630, 718098)
    passwords = possible_elve_passwords(my_range)
    strict_passwords = possible_elve_passwords(my_range, strict=True)
    print("Possible passwords with rules of Part I: ", len(passwords))
    print("Possible passwords with rules of Part II: ", len(strict_passwords))


if __name__ == "__main__":
    main()
