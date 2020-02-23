"""File containing useful functions for Day 24 of AoC_19."""

from scipy.signal import convolve2d
import numpy as np

from constants import ALIVE, DEAD

def calculate_biodiversity(state: np.array, alive_symbol=ALIVE):
    """Given some state, calculates its biodiversity."""
    alive_array = (state == ALIVE)
    vector = alive_array.reshape(-1)
    list_of_cell_values = list(vector)
    return sum([value*(2**index) for index, value 
                in enumerate(list_of_cell_values)])

def string_repr(state: np.array) -> str:
    """Turns np.array into string format."""
    return "\n".join(["".join([element for element in row])
                      for row in state])

def point(direction, coord: tuple) -> tuple:
    """
    Gets coords of point below, above, right 
    or left of coordinate in 2 dimensions
    """
    if direction == "right_of":
        return (coord[0], coord[1] + 1)
    if direction == "left_of":
        return (coord[0], coord[1] - 1)
    if direction == "above":
        return (coord[0] - 1, coord[1])
    if direction == "below":
        return (coord[0] + 1, coord[1])