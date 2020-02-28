from tqdm import tqdm

from classes.space_deck import SpaceDeck
from classes.card_tracker import CardTracker


def main():
    with open("testfiles/example_4.in", "r") as f:
        input_instructions = f.read()
    my_deck = SpaceDeck(num_cards=10_007)
    my_deck.shuffle(input_instructions)
    print(my_deck.ordering.index(2019))

    my_deck = CardTracker(num_cards=119_315_717_514_047, specific_card=2020)
    my_deck.shuffle_multiple_times(times=101_741_582_076_661,
                                   instructions=input_instructions)
    print(my_deck.card_position)


if __name__ == "__main__":
    main()

# 14_914_464_689_255
