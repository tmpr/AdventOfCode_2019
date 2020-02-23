"""File containing only the BugField class."""

import numpy as np
from scipy.signal import convolve2d

from functions import calculate_biodiversity, string_repr
from constants import ALIVE, DEAD


class BugField:

    def __init__(self, field_as_string: str):
        self.state = self.get_initial_state(field_as_string)
        self.first_rec_state = self.find_first_recurrent_state()

    def get_initial_state(self, field_as_string: str) -> np.array:
        """Transforms input string to numpy array."""
        inital_state = np.array([list(row)for row 
                                 in field_as_string.splitlines()],
                                 dtype=np.object_)
        return inital_state

    def forward(self, minutes=1):
        """
        Simulates minutes, i.e. applies rules and changes the 
        current state accordingly.
        """
        for _ in range(minutes):
            self.state = self.get_next_state(self.state)

    def find_first_recurrent_state(self) -> np.array:
        """
        Lets 'minutes' pass until it finds some state
        that has happened before and returns it. 
        """
        no_recurrent_state = True
        past_states = list()
        while no_recurrent_state:

            # For hashability, turn it back into a string.
            state_as_string = string_repr(self.state)
            if state_as_string in past_states:
                return self.state
            past_states.append(state_as_string)
            self.forward()
    
    def get_next_state(self, symbol_array: np.array) -> np.array:
        """
        Takes in some array containing symbols representing bugs and dead cells
        and applies the rules to the array and returns it. 
        """
        value_array = (symbol_array == ALIVE)
        adjacency_kernel = [
            [0, 1, 0],
            [1, 8, 1],
            [0, 1, 0]
        ]
        
        convolved_array = convolve2d(value_array, adjacency_kernel, mode="same")
        alive_array = ((convolved_array == 9) +
                        (convolved_array == 1) +
                        (convolved_array == 2))

        symbol_array[alive_array == True] = ALIVE
        symbol_array[alive_array == False] = DEAD
        return symbol_array
