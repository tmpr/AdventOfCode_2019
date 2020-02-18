"""Code containing the Moon class."""
import numpy as np


class Moon:
    """Model of a moon. Initial velocity is 0 on all axes."""
    def __init__(self, posititon):

        if len(posititon) != 3:
            raise ValueError("Position must be iterable of size 3.")
        self.position = np.array(posititon, dtype="int64")
        self.velocity = np.array([0, 0, 0], dtype="int64")

    def apply_gravity(self, other):
        """
        Takes other moon instance and changes velocity
        accordingly.
        """
        differences = other.position - self.position
        velocity_changes = np.array([difference // abs(difference) for
                                     difference in differences], dtype="int64")
        self.velocity += velocity_changes

    def apply_velocity(self):
        """According to current velocity, updates the position."""
        self.position += self.velocity

    def return_total_energy(self):
        """Returns product of sum(abs(position)) and sum(abs(velocity))."""
        return sum(abs(self.position)) * sum(abs(self.velocity))

    def return_axis(self, axis: int):
        """Returns current position and velocity in given axis"""
        return self.position[axis], self.velocity[axis]
