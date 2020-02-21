"""File containing only the SpaceImage class."""

import numpy as np
from matplotlib import pyplot as plt


class SpaceImage:
    """Model of a Space-Image."""
    def __init__(self, input_string: str):
        raw_array = np.array(list(input_string), dtype=np.uint8)
        self.shaped_array = raw_array.view()
        self.shaped_array.shape = (-1, 150)

    def max_layer_count(self):
        """
        Returns the amount of pixels of the 
        layer with most non-transparent pixels.
        """
        layer_pixels = [(np.count_nonzero(self.shaped_array[i]), i)
                        for i in range(100)]
        max_layer = max(layer_pixels)[1]
        max_layer_pixels = (np.count_nonzero(self.shaped_array[max_layer] == 1) *
                            np.count_nonzero(self.shaped_array[max_layer] == 2))
        return max_layer_pixels

    def visualize(self):
        """Decodes image and plots it."""
        processed_image = np.array([self.nontransparent_pixel(0, index)
                                    for index, pixel in enumerate(self.shaped_array[0])])
        processed_image.shape = (6, 25)
        plt.imshow(processed_image)
        plt.show()

    def nontransparent_pixel(self, current_layer, pixel_position):
        """
        Given pixel, iterates through layers and finds the first
        non-transparent pixel.
        """
        if self.shaped_array[current_layer][pixel_position] != 2:
            return self.shaped_array[current_layer][pixel_position]
        else:
            return self.nontransparent_pixel(current_layer + 1,
                                             pixel_position)
