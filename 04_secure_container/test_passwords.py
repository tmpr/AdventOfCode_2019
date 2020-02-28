"""
PyTest to Day 04 of the Advent of Code 2019.
Title: 'Secure Container'
URL: https://adventofcode.com/2019/day/04
Author: tmpr
Date: 20th of February
"""

import pytest
import os

from functions import _is_valid_password

class TestValidElvePassword:

    def test_repdigit(self):
        assert _is_valid_password(111111)
        assert not _is_valid_password(111111, strict=True)
            
    def test_non_monotonous_number(self):
        assert not _is_valid_password(223450)
    
    def test_number_without_double_digit(self):
        assert not _is_valid_password(123789)
    
    def test_number_with_tripple_digit(self):
        assert _is_valid_password(123444)
        assert not _is_valid_password(123444, strict=True)
                    
    def test_valid_number_1(self):
        assert _is_valid_password(112233)
        assert _is_valid_password(112233, strict=True)

    def test_valid_number_2(self):
        assert _is_valid_password(111122)
        assert _is_valid_password(111122, strict=True)

    
    
    