"""
Solution to Day 9 of the Advent of Code 2019.
Title: 'Sensor Boost'
URL: https://adventofcode.com/2019/day/9
Author: tmpr
Date: 17th of February
"""

from array import array
import numpy as np


class IntComputer:
    """
    Model of an IntComputer from the 'Advent of Code 2019'
    coding challenge. https://adventofcode.com/2019/day/9.

    Supports OP-codes 01-09 and 99. and parameter modes 0, 1 and 2.
    Memory supports signed 8-byte integers.
    """
    def __init__(self, intcodes_as_string):
        """
        Initializes an instance of IntComputer from string
        of intcodes and extends its memory with 3 million 
        zeros.
        """
        self.initial_intcodes = array("q", [int(integer) for integer
                        in intcodes_as_string.split(",")])
        self.initial_intcodes.extend(list(np.zeros(3000000, dtype="int64")))

    def run_program(self, input_instruction, phase_settings=0, phase_mode=False):
        """
        Runs a given IntCode program. 
        Phase mode is used for specific programs.
        """
        running = True
        position = 0
        self.intcodes = self.initial_intcodes[:]
        self.relative_base = 0

        while running:
            modes = self.get_parameter_modes(self.intcodes[position])
            opcode = (modes[-2:])

            mode_1 = modes[-3]
            mode_2 = modes[-4]
            mode_3 = modes[-5]

            if opcode == array("i", [9, 9]):
                break


            param_1 = self.intcodes[position + 1]
            param_2 = self.intcodes[position + 2]
            param_3 = self.intcodes[position + 3]

            if opcode == array("i", [0, 1]):
                self.intcodes[self._get_value(param_3, mode_3, inmode=True)] = \
                             (self._get_value(param_1, mode_1) +
                              self._get_value(param_2, mode_2))
                position = position + 4

            elif opcode == array("i", [0, 2]):
                self.intcodes[self._get_value(param_3, mode_3, inmode=True)] = \
                             (self._get_value(param_1, mode_1) *
                              self._get_value(param_2, mode_2))
                position = position + 4

            elif opcode == array("i", [0, 3]):
                if phase_mode: # First input is phase setting if phase mode.
                    assert False
                    self.intcodes[param_1] = phase_settings
                else:
                    self.intcodes[self._get_value(param_1, mode_1, inmode=True)] \
                                                = input_instruction
                    position = position + 2

            elif opcode == array("i", [0, 4]):
                last_output = self._get_value(param_1, mode_1)
                yield last_output
                position = position + 2

            elif opcode == array("i", [0, 5]):
                if self._get_value(param_1, mode_1) != 0:
                    position = self._get_value(param_2, mode_2)
                else:
                    position = position + 3

            elif opcode == array("i", [0, 6]):
                if self._get_value(param_1, mode_1) == 0:
                    position = self._get_value(param_2, mode_2)
                else:
                    position = position + 3

            elif opcode == array("i", [0, 7]):
                if self._get_value(param_1, mode_1) < self._get_value(param_2, mode_2):
                    self.intcodes[self._get_value(param_3, mode_3, inmode=True)] = 1
                else:
                    self.intcodes[self._get_value(param_3, mode_3, inmode=True)] = 0
                position = position + 4

            elif opcode == array("i", [0, 8]):
                if self._get_value(param_1, mode_1) == self._get_value(param_2, mode_2):
                    self.intcodes[self._get_value(param_3, mode_3, inmode=True)] = 1
                else:
                    self.intcodes[self._get_value(param_3, mode_3, inmode=True)] = 0
                position = position + 4

            elif opcode == array("i", [0, 9]):
                self.relative_base += self._get_value(param_1, mode_1)
                position = position + 2

            else:
                raise ValueError(f"Encountered unsupported OP-Code: {opcode}")

        return last_output

    def _get_value(self, parameter, parameter_mode, inmode=False):
        """
        Retrieves value according to the parameter
        and its mode. Supported parameter_modes: 

        0:'Position mode'  := Retrieves value at position [parameter].
        1:'Immediate mode' := Retrieves the parameter itself.
        2:'Relative mode'  := Retrieves value at position 
                              [parameter + relative base].
        """
        if parameter_mode == 0:
            return self.intcodes[parameter] if not inmode else parameter
        elif parameter_mode == 1:
            return parameter
        elif parameter_mode == 2:
            return self.intcodes[parameter + self.relative_base] if not inmode else parameter + self.relative_base
        else:
            raise ValueError(f"Encountered invalid parameter mode: {parameter_mode}")

    def get_parameter_modes(self, opcode):
        """Splits up an OP-code into it's parameter modes and
        returns them as an array:
         (mode_3, mode_2, mode_0, op_code, op_code)"""
        parameter_modes = array("i",[0, 0, 0, 0, 0])
        split_opcode = list(str(opcode))
        for i in range(len(split_opcode)):
            parameter_modes[-(i + 1)] = int(split_opcode[-(i + 1)])
        return parameter_modes

def main(path_to_intocode):
    with open(path_to_intocode) as f:
        intcodes_string = f.read()
    my_intcomputer = IntComputer(intcodes_string)
    output_generator = my_intcomputer.run_program(input_instruction=1)
    for output in output_generator:
        print(output)

if __name__ == "__main__":
    main("intcodes_09.txt")
