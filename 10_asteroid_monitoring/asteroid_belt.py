import numpy as np
from asteroid import Asteroid

class AsteroidBelt:
    """Model of an asteroid belt."""
    def __init__(self, input_field):
        self.matrix = self.format_input_to_matrix(input_field)
        self.asteroids = [Asteroid(tuple(coordinates), self) for coordinates
                          in np.argwhere(self.matrix == 1)]
        self.generate_asteroid_perspectives()
        self.best_asteroid = max(
            self.asteroids,
            key=lambda asteroid: asteroid.visible_asteroid_count)

    def format_input_to_matrix(self, input_field):
        """Formats input to 2-dimensional matrix."""
        list_of_lists = [[1 if char == "#" else 0 for char in row]
                         for row in input_field.splitlines()]
        matrix = np.array(list_of_lists)
        if len(matrix.shape) != 2:
            raise ValueError("Input cannot be transformed into matrix.")
        return np.transpose(matrix)

    def generate_asteroid_perspectives(self) -> list:
        """Generates the perspective of all asteroids."""
        for asteroid in self.asteroids:
            asteroid.generate_perspective()