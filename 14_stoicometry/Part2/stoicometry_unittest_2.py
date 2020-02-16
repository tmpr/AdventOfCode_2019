import unittest
import os

from stoicometry import compute_ore_cost, compute_possible_fuel_output

class ComputeOreCostTest(unittest.TestCase):
    """
    Unittests for the Advent of Code task: 
    'Space Stoicometry'.
    """
    def test_easy_example(self):
        with open(os.path.join("example_files", "easy_example.txt"), "r") as f:
              easy_example = f.read()
        self.assertEqual(compute_ore_cost(easy_example), 31)
        
    
    def test_medium_example(self):
        with open(os.path.join("example_files", "medium_example.txt"), "r") as f:
              medium_example = f.read()
              self.assertEqual(compute_ore_cost(medium_example), 165)

    def test_large_example_1(self):
        with open(os.path.join("example_files", "large_ex1.txt"), "r") as f:
              large_ex1 = f.read()
              self.assertEqual(compute_ore_cost(large_ex1), 13312)
            #   self.assertEqual(
            #       compute_possible_fuel_output(1_000_000_000_000, large_ex1), 82892753)

    def test_large_example_2(self):
        with open(os.path.join("example_files", "large_ex2.txt"), "r") as f:
              large_ex2 = f.read()
              self.assertEqual(compute_ore_cost(large_ex2), 180697)
            #   self.assertEqual(
            #       compute_possible_fuel_output(1_000_000_000_000, large_ex2), 5586022)
    
    def test_large_example_3(self):
        with open(os.path.join("example_files", "large_ex3.txt"), "r") as f:
              large_ex3 = f.read()
              self.assertEqual(compute_ore_cost(large_ex3), 2210736)
            #   self.assertEqual(
            #       compute_possible_fuel_output(1_000_000_000_000, large_ex3), 460664)