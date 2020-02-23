"""File containing only the RecursiveBugField class."""

import numpy as np
import os

from functions import point
from constants import COORD_NEXT_TO_MIDDLE, DEAD, ALIVE
from constants import OPPOSITE, EMPTY_FIELD
from bug_field import BugField


class RecursiveBugField(BugField):
    """
    BugField which is theoretically infinite in size and has
    another RecursiveBugField as its middle cell, while being
    the middle cell of another RecursiveBugField, i.e. the RBF
    has a super- and a subfield.

    Due to limitations of Python, Infinity cannot be modelled,
    thus specify a `max_recursion_depth`, which determines how
    many 'layers' the field has in each direction. 
    """

    def __init__(self, field_as_string: str, depth=0, sub_field=None,
                 super_field=None, max_recursion_depth=50):
        self.state = self.get_initial_state(field_as_string)
        self.depth = depth
        self.max_recursion = max_recursion_depth

        self.create_other_field(sub_field, "sub")
        self.create_other_field(super_field, "super")

        if self.sub_field:
            self.state[2, 2] = self.sub_field

    def create_other_field(self, other_field, mode):
        """
        If allowed by the max recursion depth, creates super- or subfield.

        - Modes: 
        `'super'` - Creates superfield. Needs passed param `super_field`.\n
        `'sub'` - Creates subfield. Needs passed param `sub_field.`\n
        """
        if mode == "sub":
            if self.depth == - self.max_recursion:
                self.sub_field = None
            elif other_field:
                self.sub_field = other_field
            else:
                self.sub_field = RecursiveBugField(EMPTY_FIELD,
                                    depth=self.depth - 1,
                                    super_field=self,
                                    max_recursion_depth=self.max_recursion)

        elif mode == "super":
            if self.depth == self.max_recursion:
                self.super_field = None
            elif other_field:
                self.super_field = other_field
            else:
                self.super_field = RecursiveBugField(EMPTY_FIELD,
                                        depth=self.depth + 1,
                                        sub_field=self,
                                        max_recursion_depth=self.max_recursion)
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def forward(self, minutes=1):
        """Advances entire recursive field given amount of minutes."""
        for _ in range(minutes):
            highest_field = self.get_highest_field()
            highest_field.compute_next_states()
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
        self.next_state = self.get_next_state()

    def update_states(self):
        """Assigns the value of the next state to the current state."""
        if self.sub_field:
            self.sub_field.update_states()
        self.state = self.next_state

    def get_next_state(self):
        """
        Applies rules for own state of the field and 
        thenceforth returns that computed next state.
        """
        next_state = np.array(self.state)

        y_length, x_length = self.state.shape
        for y_coord in range(y_length):
            for x_coord in range(x_length):
                coord = (y_coord, x_coord)

                if coord == (2, 2):
                    continue

                adj_bugs = 0

                adj_bugs += self.alive_neighbors(coord, "right_of")
                adj_bugs += self.alive_neighbors(coord, "left_of")
                adj_bugs += self.alive_neighbors(coord, "below")
                adj_bugs += self.alive_neighbors(coord, "above")

                if self.state[coord] == ALIVE:
                    if adj_bugs == 1:
                        if abs(self.depth) == self.max_recursion:
                            raise Warning("Altered outermoust level.")
                        next_state[coord] = ALIVE
                    else:
                        next_state[coord] = DEAD
                else:
                    if adj_bugs in [1, 2]:
                        if abs(self.depth) == self.max_recursion:
                            raise Warning("Altered outermoust level.")
                        next_state[coord] = ALIVE
                    else:
                        next_state[coord] = DEAD

        return next_state

    def total_bugs(self):
        """Returns amount of entire recursive field."""
        highest_field = self.get_highest_field()
        total_bugs = highest_field.number_of_bugs()
        return total_bugs

    def number_of_bugs(self):
        if self.sub_field:
            bugs_below = self.sub_field.number_of_bugs()
        else:
            bugs_below = 0
        return np.count_nonzero(self.state == ALIVE) + bugs_below

    def alive_neighbors(self, coordinate: tuple, direction: str):
        """
        Given some coordinate, returns its alive neighbors in some
        direction.
        """
        alive_neighbors = 0
        try:
            desired_point = point(direction, coordinate)
            if desired_point[0] < 0 or desired_point[1] < 0:
                raise IndexError
            elif self.state[desired_point] == ALIVE:
                alive_neighbors += 1
            elif self.state[desired_point] == DEAD:
                pass
            else:
                if self.sub_field:
                    alive_neighbors += self.sub_field.edge_value(
                        OPPOSITE[direction])
        except IndexError:
            adjacent_super_coord = COORD_NEXT_TO_MIDDLE[direction]
            if self.super_field:
                if self.super_field.state[adjacent_super_coord] == ALIVE:
                    alive_neighbors += 1
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

    def __repr__(self):
        return "BF{self.depth}"
