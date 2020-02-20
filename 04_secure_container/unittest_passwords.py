"""
Unittest to Day 04 of the Advent of Code 2019.
Title: 'Secure Container'
URL: https://adventofcode.com/2019/day/04
Author: tmpr
Date: 20th of February
"""

import unittest

from functions import _is_valid_password

class ValidElvePasswordTest(unittest.TestCase):

    def test_repdigit(self):
        self.assertTrue(_is_valid_password(111111))
        self.assertFalse(_is_valid_password(111111, strict=True),
                        msg="No strict double digit.")

    def test_non_monotonous_number(self):
        self.assertFalse(_is_valid_password(223450),
                         msg="Not non-decreasing.")
    
    def test_number_without_double_digit(self):
        self.assertFalse(_is_valid_password(123789),
                         msg="No double digit.")
    
    def test_number_with_tripple_digit(self):
        self.assertTrue(_is_valid_password(123444))
        self.assertFalse(_is_valid_password(123444, strict=True), 
                         msg="No strict double digit.")
    
    def test_valid_number_1(self):
        self.assertTrue(_is_valid_password(112233))
        self.assertTrue(_is_valid_password(112233, strict=True))

    def test_valid_number_2(self):
        self.assertTrue(_is_valid_password(111122))
        self.assertTrue(_is_valid_password(111122, strict=True))

    
    
    