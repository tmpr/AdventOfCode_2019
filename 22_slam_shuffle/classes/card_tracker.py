from classes.space_deck import SpaceDeck


class CardTracker(SpaceDeck):
    """
    Specific Type of SpaceDeck which only keeps track of
    where some specific card is in a deck.
    """

    def __init__(self, num_cards: int, specific_card: int):
        self.max_index = num_cards - 1
        self.card_position = specific_card
        self.original_positon = specific_card

    def _into_new_stack(self):
        """
        Keeps track of where the card would go if the deck
        were to be reversed.
        """
        self.card_position = self.max_index - self.card_position

    def shuffle_multiple_times(self, times: int, instructions: str):
        """Shuffles deck multiple times."""
        current_iteration = 0
        while current_iteration <= times:
            old_position = self.card_position
            self.shuffle(instructions)
            current_iteration += 1

            print(f"""After {current_iteration} shuffle{
                    ('s' if current_iteration > 1 else '')}.""")

            # displacement = self.card_position - old_position
            # print(f"Old position: {old_position}.")
            # print(f"New position: {self.card_position}.")
            # print(f"Displacement: {displacement}.\n")
            # input()

            # Since the card position is independent of its
            # neighbors, we can work with cycles.
            if self.card_position == self.original_positon:
                cycle_length = current_iteration
                print("Found cycle length: ", cycle_length)
                current_iteration = times - times % cycle_length
                print("Jumped to iteration ", current_iteration)

    def _cut(self, number: int):
        """Keeps track of where the card goes after a cut."""
        if number > 0:
            if (number - 1) >= self.card_position:
                self.card_position = self.max_index - (number - 1
                                                       - self.card_position)
            else:
                self.card_position -= number
        else:
            if (self.max_index) <= self.card_position:
                self.card_position = self.card_position - \
                    (self.max_index - (- number - 1))
            else:
                self.card_position -= number

    def _with_increment(self, increment: int):
        """
        Keeps track of where the card would go after a deal with increment.
        """
        position = (increment * self.card_position) % (self.max_index + 1)
        self.card_position = position
