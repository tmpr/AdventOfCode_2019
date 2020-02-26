from collections import deque
import numpy as np
from numba import jit

class SpaceDeck:

    def __init__(self, num_cards: int):
        self.num_cards = num_cards
        self.ordering = deque(range(self.num_cards), maxlen=self.num_cards)

    def shuffle(self, instructions_string: str):
        """
        Given some list of instructions, performs them in a row, 
        i.e. shuffles the deck.
        """
        instructions = self._format_instructions(instructions_string)
        for instruction in instructions:
            self._follow(instruction)

    def _format_instructions(self, instructions_string: str) -> list:
        """Turns raw instructions into usable list of lists."""
        lines = instructions_string.splitlines()
        instructions = [self._format_single_instruction(instruction)
                        for instruction in lines]
        return instructions

    def _format_single_instruction(self, instruction: str) -> list:
        """Formats a single line of the input."""
        instruction_words = instruction.split()
        if instruction_words[0] == "cut":
            return ["cut", int(instruction_words[1])]
        else:
            try:
                # Deal with increment (int)
                instruction_words[-1] = int(instruction_words[-1])
                return [" ".join(instruction_words[:-1]), instruction_words[-1]]
            except ValueError:  
                # Deal into new stack
               return instruction
            
    
    def _follow(self, instruction):
        """Follows some shuffling instruction."""
        if instruction[0] == "cut":
            self._cut(instruction[1])
        elif instruction == "deal into new stack":
            self._into_new_stack()
        elif instruction[0] == "deal with increment":
            self._with_increment(instruction[1])
        else:
            raise ValueError("Encountered unknown instruction: ", instruction)

    
    def _cut(self, number: int):
        """Takes some cut of the deck and puts it onto the other deck."""
        if number > 0:
            cut = (self.ordering.popleft() for _ in range(number))
            self.ordering.extend(cut)
        else:
            cut = (self.ordering.pop() for _ in range(-number))
            self.ordering.extendleft(cut)

    def _into_new_stack(self):
        """Reverses deck."""
        self.ordering.reverse()

    def _with_increment(self, increment: int):
        """Deals with increment."""
        new_ordering = np.array(range(self.num_cards))
        position = 0
        while self.ordering:
            new_ordering[position] = self.ordering.popleft()
            position = (position + increment) % self.num_cards 
        self.ordering = deque(new_ordering)
