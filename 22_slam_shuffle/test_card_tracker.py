import pytest
import os

from classes.card_tracker import CardTracker

if os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
    RP = ""
else:
    RP = os.path.dirname(os.path.realpath(__file__))

class TestCardTrackerBasics:

    def test_deal_into_new_stack(self):
        instruction_string = "deal into new stack"
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 6

    def test_cut_positive_card_out_of_cut(self):
        instruction_string = "cut 3"
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 0

    def test_cut_positive_card_in_cut(self):
        instruction_string = "cut 3"
        my_deck = CardTracker(num_cards=10, specific_card=2)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 9

    def test_cut_negative_card_out_of_cut(self):
        instruction_string = "cut -4"
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 7

    def test_cut_negative_card_in_cut(self):
        instruction_string = "cut -4"
        my_deck = CardTracker(num_cards=10, specific_card=9)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 3

    def test_deal_with_increment(self):
        instruction_string = "deal with increment 3"
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 9


class TestCardTrackerExamples:

    def test_example_1(self):
        with open(os.path.join(RP, "testfiles", "example_1.in"), "r") as f:
            instruction_string = f.read()
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 1

    def test_example_2(self):
        with open(os.path.join(RP, "testfiles", "example_2.in"), "r") as f:
            instruction_string = f.read()
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 0

    def test_example_3(self):
        with open(os.path.join(RP, "testfiles", "example_3.in"), "r") as f:
            instruction_string = f.read()
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 1

    def test_example_4(self):
        with open(os.path.join(RP, "testfiles", "example_4.in"), "r") as f:
            instruction_string = f.read()
        my_deck = CardTracker(num_cards=10, specific_card=3)
        my_deck.shuffle(instruction_string)
        assert my_deck.card_position == 8