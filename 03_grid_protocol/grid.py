"""File containing the Grid-class."""

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

class Grid:
    """Model of a grid with wires running through it."""

    def __init__(self, input_string: str):
        wire_instructions = self.input_to_instructions(input_string)
        self.wire_paths = [self.create_wire_path(instructions)
                           for instructions in wire_instructions]

    def input_to_instructions(self, input_string: str) -> tuple:
        """Returns 2 lists of instructions from input string."""
        instruction_strings = input_string.splitlines()
        wire_instructions = [instruction_string.split(",") for
                             instruction_string in instruction_strings]
        return wire_instructions

    def create_wire_path(self, instructions: list) -> list:
        """Given instructions, creates wirepath as a list of coords."""
        wire_path = []
        latest_point = (0, 0)
        for instruction in instructions:
            wire_path.extend(
                self.follow_instruction(
                    latest_point, instruction))
            latest_point = wire_path[-1]
        return wire_path

    def follow_instruction(self, starting_point, instruction):
        """
        Given some instruction, 'walks' it and returns a list
        of coordinates passed.
        """
        direction = instruction[0]
        steps = int(instruction[1:])

        if direction == RIGHT:
            return [(starting_point[0] + step, starting_point[1])
                    for step in range(1, steps + 1)]
        elif direction == LEFT:
            return [(starting_point[0] - step, starting_point[1])
                    for step in range(1, steps + 1)]
        elif direction == UP:
            return [(starting_point[0], starting_point[1] + step)
                    for step in range(1, steps + 1)]
        elif direction == DOWN:
            return [(starting_point[0], starting_point[1] - step)
                    for step in range(1, steps + 1)]

        else:
            raise ValueError("Input contains invalid instruction.")

    def closest_intersec_dist(
            self,
            mode: str,
            wire_path1=None,
            wire_path2=None):
        """
        Finds closest intersection between two wire-paths.

        - Modes:
        `'manhattan'` - Distance is measured as the sum of x- and y-value.\n
        `'path_length'` - Distance is measured as the steps
        needed for both wire-paths to reach the intersection.
        """
        if bool(wire_path1) ^ bool(wire_path2):
            raise ValueError("Only received 1 wire path.")
        elif not (wire_path1 and wire_path2):
            wire_path1 = self.wire_paths[0]
            wire_path2 = self.wire_paths[1]

        intersections = list(set(wire_path1) & set(wire_path2))

        if mode == "manhattan":
            distances = {coord: abs(coord[0]) + abs(coord[1])
                         for coord in intersections}
        elif mode == "path_length":
            distances = {coord: wire_path1.index(coord) +
                         wire_path2.index(coord) + 2
                         for coord in intersections}
        else:
            raise ValueError(f"Invalid mode: {mode}. "
                             + "Try 'manhattan' or 'path_length.")

        clostest_intersection = min(
            distances, key=lambda coord: distances[coord])

        return distances[clostest_intersection]
