"""Constants needed for solving Day 24."""

import os

ALIVE = "#"
DEAD = "."
OPPOSITE = {
    "above" : "bottom",
    "below" : "top",
    "right_of" : "left",
    "left_of" : "right"
}
COORD_NEXT_TO_MIDDLE = {
    "below" : (3, 2),
    "above" : (1, 2),
    "right_of": (2, 3),
    "left_of" : (2, 1)
}

with open(os.path.join("inputs", "empty_field.in"), "r") as f:
    empty = f.read()
EMPTY_FIELD = empty