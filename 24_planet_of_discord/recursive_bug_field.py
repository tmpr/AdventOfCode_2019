"""File containing only the RecursiveBugField class."""

import numpy as np

from bug_field import BugField
from constants import ALIVE, COORD_NEXT_TO_MIDDLE, DEAD, EMPTY_FIELD, OPPOSITE
from functions import point


class RecursiveBugField(BugField):
    """
    BugField which is theoretically infinite in size and has
    another RecursiveBugField as its middle cell, while being
    the middle cell of another RecursiveBugField, i.e. the RBF
    has a super- and a subfield.
    """

    def __init__(self, field_as_string: str, sub_field=None, super_field=None):
        self.state = self.get_initial_state(field_as_string)

        self.super_field = super_field
        self.sub_field = sub_field

        self.state[2, 2] = "?"

    def forward(self, minutes=1):
        """Advances entire recursive field given amount of minutes."""
        for _ in range(minutes):
            highest_field = self.get_highest_field()
            highest_field.compute_next_states()

            # When computing next states, 
            # the highest field might change.
            highest_field = self.get_highest_field()
            highest_field.update_states()

    def get_highest_field(self):
        """Returns field which has no super field."""
        if self.super_field:
            return self.super_field.get_highest_field()
        else:
            return self

    def compute_next_states(self):
        """Computes next state for all fields."""
        if self.sub_field:
            self.sub_field.compute_next_states()
        self.set_next_state()

    def update_states(self):
        """Assigns the value of the next state to the current state."""
        if self.sub_field:
            self.sub_field.update_states()
        self.state = self.next_state

    def set_next_state(self):
        """Sets next state according to rules."""
        self.next_state = np.array(self.state)

        for coord in np.argwhere(self.state != False):
            coord = tuple(coord)
            if coord == (2, 2): 
                continue

            adj_bugs = sum([self.alive_neighbors("right_of", coord),
                            self.alive_neighbors("left_of", coord),
                            self.alive_neighbors("below", coord),
                            self.alive_neighbors("above", coord)])

            if self.state[coord] == ALIVE:
                if adj_bugs == 1:
                    self.next_state[coord] = ALIVE
                else:
                    self.next_state[coord] = DEAD
            else:
                if adj_bugs in [1, 2]:
                    self.next_state[coord] = ALIVE
                else:
                    self.next_state[coord] = DEAD

    def total_bugs(self):
        """Returns amount of bugs of entire recursive field."""
        highest_field = self.get_highest_field()
        total_bugs = highest_field.number_of_bugs()
        return total_bugs

    def number_of_bugs(self):
        """Returns number of bugs of single bugfield."""
        if self.sub_field:
            bugs_below = self.sub_field.number_of_bugs()
        else:
            bugs_below = 0
        return np.count_nonzero(self.state == ALIVE) + bugs_below

    def alive_neighbors(self, direction: str, coordinate: tuple):
        """
        Given some coordinate, returns its alive neighbors in some
        direction.
        """
        alive_neighbors = 0
        try:
            other_point = point(direction, coordinate)
            if other_point[0] < 0 or other_point[1] < 0:
                raise IndexError
            elif self.state[other_point] == ALIVE:
                alive_neighbors = 1
            elif self.state[other_point] == DEAD:
                pass

            else:
                if self.sub_field:
                    alive_neighbors = self.sub_field.edge_value(
                        OPPOSITE[direction])
                elif self.state[coordinate] == ALIVE:
                    self.sub_field = RecursiveBugField(EMPTY_FIELD,
                                                       super_field=self)
                    self.sub_field.set_next_state()

        # Access super field.
        except IndexError: 
            adjacent_super_coord = COORD_NEXT_TO_MIDDLE[direction]
            if self.super_field:
                if self.super_field.state[adjacent_super_coord] == ALIVE:
                    alive_neighbors = 1
            elif self.state[coordinate] == ALIVE:
                self.super_field = RecursiveBugField(EMPTY_FIELD,
                                                     sub_field=self)
                self.super_field.set_next_state()
                                                        
        return alive_neighbors

    def edge_value(self, mode: str):
        """
        Returns the number of alive cells of given edge.\n
        Modes are `'right'`, `'left'`, `'top'`, `'bottom'`.
        """
        if mode == "top":
            return np.count_nonzero(self.state[0, :] == ALIVE)
        elif mode == "bottom":
            return np.count_nonzero(self.state[-1, :] == ALIVE)
        elif mode == "right":
            return np.count_nonzero(self.state[:, -1] == ALIVE)
        elif mode == "left":
            return np.count_nonzero(self.state[:, 0] == ALIVE)
        else:
            raise ValueError(f"Unknown edge mode: {mode}")
