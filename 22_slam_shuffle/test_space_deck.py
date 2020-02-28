import os
import pytest
from collections import deque

from classes.space_deck import SpaceDeck

if os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
    RP = ""
else:
    RP = os.path.dirname(os.path.realpath(__file__))

class TestSpaceDeckBasics:

    def test_deal_into_new_stack(self):
        instruction_string = "deal into new stack"
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_cut_positive(self):
        instruction_string = "cut 3"
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])

    def test_cut_negative(self):
        instruction_string = "cut -4"
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([6, 7, 8, 9, 0, 1, 2, 3, 4, 5])

    def test_deal_with_increment(self):
        instruction_string = "deal with increment 3"
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([0, 7, 4, 1, 8, 5, 2, 9, 6, 3])


class TestSpaceDeckExamples:

    def test_example_1(self):
        with open(os.path.join(RP, "testfiles", "example_1.in"), "r") as f:
            instruction_string = f.read()
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([0, 3, 6, 9, 2, 5, 8, 1, 4, 7])

    def test_example_2(self):
        with open(os.path.join(RP, "testfiles", "example_2.in"), "r") as f:
            instruction_string = f.read()
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([3, 0, 7, 4, 1, 8, 5, 2, 9, 6])

    def test_example_3(self):
        with open(os.path.join(RP, "testfiles", "example_3.in"), "r") as f:
            instruction_string = f.read()
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([6, 3, 0, 7, 4, 1, 8, 5, 2, 9])

    def test_example_4(self):
        with open(os.path.join(RP, "testfiles", "example_4.in"), "r") as f:
            instruction_string = f.read()
        my_deck = SpaceDeck(num_cards=10)
        my_deck.shuffle(instruction_string)
        assert my_deck.ordering == deque([9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
