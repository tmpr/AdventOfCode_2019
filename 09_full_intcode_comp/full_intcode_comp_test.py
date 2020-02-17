"""
Unittest to Day 9 of the Advent of Code 2019.
Title: 'Sensor Boost'
URL: https://adventofcode.com/2019/day/09
Author: tmpr
Date: 17th of February
"""
import os
import unittest

from int_comp_relative import IntComputer

class RelativeIntCompTest(unittest.TestCase):

    def test_copy_of_itself(self):
        intcode = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        computer_1 = IntComputer(intcode)
        self.assertEqual(list(computer_1.run_program(input_instruction=None)),
                         [int(integer) for integer in intcode.split(",")])
    
    def test_return_16_digit_number(self):
        intcode = "1102,34915192,34915192,7,4,7,99,0"
        computer = IntComputer(intcode)
        self.assertEqual(len(str(list(computer.run_program(input_instruction=None))[0])), 16)
    
    def test_large_number_in_middle(self):
        intcode = "104,1125899906842624,99"
        computer = IntComputer(intcode)
        self.assertEqual(list(computer.run_program(input_instruction=None))[0], 1125899906842624)