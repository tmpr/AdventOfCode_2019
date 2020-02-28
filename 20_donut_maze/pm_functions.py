"""
Helper functions for solving the 'Donut Maze' problem
from Advent of Code, Day 20.
"""


def point_3d(direction, coord: tuple) -> tuple:
    """Gets coords of point below, above, right or left in 3 dimensions"""
    if direction == "right_of":
        return (coord[0], coord[1], coord[2] + 1)
    if direction == "left_of":
        return (coord[0], coord[1], coord[2] - 1)
    if direction == "above":
        return (coord[0], coord[1] - 1, coord[2])
    if direction == "below":
        return (coord[0], coord[1] + 1, coord[2])


def point_2d(direction, coord: tuple) -> tuple:
    """Gets coords of point below, above, right or left in 2 dimensions"""
    if direction == "right_of":
        return (coord[0], coord[1] + 1)
    if direction == "left_of":
        return (coord[0], coord[1] - 1)
    if direction == "above":
        return (coord[0] - 1, coord[1])
    if direction == "below":
        return (coord[0] + 1, coord[1])
