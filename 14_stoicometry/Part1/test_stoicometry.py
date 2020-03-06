"""
Unittest to Day 14 of the Advent of Code 2019.
Title: 'Space Stoicometry'
URL: https://adventofcode.com/2019/day/14
Author: tmpr
Date: 16th of my_input
"""        
import os

from account import StoiciometryAccount

if os.path.dirname(os.path.realpath(__file__)) == os.getcwd():
    PATH = "example_files"
else:
    PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                      "example_files")

class TestComputeOreCost:
    
    def test_easy_example(self):
        with open(os.path.join(PATH, "easy_example.txt"), "r") as f:
              my_input = f.read()
        my_account = StoiciometryAccount(my_input)     
        assert my_account.compute_ore_cost() == 31
        
    def test_medium_example(self):
        with open(os.path.join(PATH, "medium_example.txt"), "r") as f:
              my_input = f.read()
        my_account = StoiciometryAccount(my_input)     
        assert my_account.compute_ore_cost() == 165

    def test_large_example_1(self):
        with open(os.path.join(PATH, "large_ex1.txt"), "r") as f:
              my_input = f.read()
        my_account = StoiciometryAccount(my_input)     
        assert my_account.compute_ore_cost() == 13312

    def test_large_example_2(self):
        with open(os.path.join(PATH, "large_ex2.txt"), "r") as f:
              my_input = f.read()
        my_account = StoiciometryAccount(my_input)     
        assert my_account.compute_ore_cost() == 180697
    
    def test_large_example_3(self):
        with open(os.path.join(PATH, "large_ex3.txt"), "r") as f:
              my_input = f.read()
        my_account = StoiciometryAccount(my_input)     
        assert my_account.compute_ore_cost() == 2210736