from numba import jit
import numpy as np

from space_deck import SpaceDeck

class CardTracker(SpaceDeck):

    def __init__(self, num_cards: int, specific_card: int):
        self.max_index = num_cards - 1
        self.card_position = specific_card
    
    def shuffle(self, instructions_string: str):
        instructions = self._format_instructions(instructions_string)
        for idx, instruction in enumerate(instructions):
            if instruction[0] == "cut":
                instructions[idx][0] = 0
            elif instruction == "deal into new stack":
                instruction = 1
            else:
                instruction[0] = 2
                
        self.card_position = follow_all(instructions, self.max_index, self.card_position)

@jit
def follow_all(instructions, max_index, card_position):
    for instruction in instructions:
        card_position = _follow(instruction, max_index, card_position)
    return card_position

@jit
def _follow(instruction, max_index, card_position):
    if instruction == 0:
        card_position = _cut(instruction[1], 
                        max_index, card_position)
    elif instruction == 1:
        card_position = _into_new_stack(max_index, card_position)
    elif instruction[0] == 2:
        card_position = _with_increment(instruction[1], card_position, max_index)
    return card_position

@jit(nopython=True)
def _into_new_stack(max_index, card_position):
    return max_index - card_position

@jit(nopython=True)
def _cut(number: int, max_index, card_postion):
    if number > 0:
        if (number - 1) >= card_position:
            card_position = max_index - (number - 1
                                                    - card_position)
        else: 
            card_position -= number
    else:
        if (max_index ) <= card_position:
            card_position = card_position - (max_index - (- number - 1)) 
        else:
            card_position -= number
    
    return card_position

@jit(nopython=True)
def _with_increment(increment: int, card_position, max_index):
    return (increment * card_position) % (max_index + 1)

