"""Utility functions for the N-Body problem."""
from collections.abc import Iterable

def lowest_common_multiple(numbers: Iterable):
    """Returns the lowest common multiple of multiple numbers."""
    remaining_factors = list(numbers)
    current_factor = remaining_factors.pop()
    while remaining_factors:
        current_factor = lcm(current_factor, remaining_factors.pop())
    return current_factor

# Thanks to endolith (@endolith on github)
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
