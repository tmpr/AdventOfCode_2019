"""Utility functions for asteroid monitoring. By tmpr."""
import numpy as np
from math import cos, sin

def get_magnitude(vector):
    """Calculates length of some vector."""
    vector = np.array(vector)
    return np.power(np.sum(vector**2), 0.5)


def calculate_unit_vector(vector, decimal_precision: int):
    """
    Given some vector, calculates the unit vector,
    rounds it to given precision and returns it as tuple.
    """
    unit_vector = vector / get_magnitude(vector)

    # With precision too high, it's hard to find "equal"
    # unit_vectors. Thus round.

    unit_vector[0] = round(unit_vector[0], decimal_precision)
    unit_vector[1] = round(unit_vector[1], decimal_precision)

    return tuple(unit_vector)


def vector_between(coord_a, coord_b):
    """Return vector between two points as a tuple."""
    return tuple(np.array(coord_a) - np.array(coord_b))

def update_direction_and_phi(old_laser_direction, phi):
    """
    Changes the angle of the direction by a very small amount. 
    Returns `(new_direction, new_phi)`.
    """
    new_laser_direction = (round(cos(phi), 3), round(sin(phi), 3))
    while new_laser_direction == old_laser_direction:
        phi += 0.00001
        new_laser_direction = (round(cos(phi), 3), round(sin(phi), 3))
    return new_laser_direction, phi


