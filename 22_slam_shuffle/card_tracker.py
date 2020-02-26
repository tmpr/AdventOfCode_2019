from space_deck import SpaceDeck

class CardTracker(SpaceDeck):

    def __init__(self, num_cards: int, specific_card: int):
        self.max_index = num_cards - 1
        self.card_position = specific_card
        self.original_positon = specific_card
    
    def _into_new_stack(self):
        self.card_position = self.max_index - self.card_position

    def shuffle_multiple_times(self, times: int, instructions: str):
        current_iteration = 0
        while current_iteration < times:
            if not current_iteration % 10_000:
                print(current_iteration)
            
            self.shuffle(instructions)
            current_iteration += 1
            
            # Since the card position is independent of its 
            # neighbors, we can work with cycles.
            if self.card_position == self.original_positon:
                cycle_length = current_iteration
                print("Found cycle length: ", cycle_length)
                current_iteration = times % cycle_length
                print("Jumped to iteration ", current_iteration)

    
    def _cut(self, number: int):
        if number > 0:
            if (number - 1) >= self.card_position:
                self.card_position = self.max_index - (number - 1
                                                        - self.card_position)
            else: 
                self.card_position -= number
        else:
            if (self.max_index ) <= self.card_position:
                self.card_position = self.card_position - (self.max_index - (- number - 1)) 
            else:
                self.card_position -= number

    def _with_increment(self, increment: int):
        position = (increment * self.card_position) % (self.max_index + 1)
        self.card_position = position

