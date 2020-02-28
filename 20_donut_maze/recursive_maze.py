"""File containing the RecursiveMaze class."""

import networkx as nx
import numpy as np

from pm_functions import point_3d

PATH = "."
EMPTY = " "


class RecursiveMaze:
    """
    Model of a multidimensional Portal. Portals on the inside lead
    down one layer, outside Portals lead one layer up.

    `depth` should be a natural number representing the amount
    of layers the Maze consists of. 
    """

    def __init__(self, input_field: str, depth: int):
        """ 
        Initialize instance of PortalMaze. Creates an np.array
        and a graph containing all paths.
        """
        self.maze = self._file_to_matrix(input_field, depth)

        # Determine the rim of the labyrinth.
        self.rim_x = self.maze.shape[2] - 4
        self.rim_y = self.maze.shape[1] - 4

        self.graph = nx.Graph()

        # Connect Path / points
        self.path_coordinates = np.argwhere(self.maze == PATH)
        self._build_path()

        # Determine Portal points and connect them to corresponding
        # other dimension.
        self.merge_portals_to_path()
        self.connect_portals()

        start = tuple(np.argwhere(self.maze == "AA")[0])
        goal = tuple(np.argwhere(self.maze == "ZZ")[0])

        try:
            self.shortest_path_length = nx.shortest_path_length(
                self.graph, start, goal)
        except nx.NetworkXNoPath:
            self.shortest_path_length = None

    def _file_to_matrix(self, input_field: str, depth: int) -> np.char.array:
        """
        Turns input .txt file representing the maze to numpy matrix.
        """
        maze_rows = input_field.splitlines()
        maze_lists = [list(row) for row in maze_rows]
        maze = np.array(maze_lists)
        maze = np.pad(maze, pad_width=1, constant_values=EMPTY)

        multidim_maze = np.char.array([np.char.array(maze, itemsize=2)
                                       for _ in range(depth)])
        return multidim_maze

    def _build_path(self):
        """Connects all path coord together into a graph."""
        for point_3d in self.path_coordinates:
            self.connect_point_with_neighbors(point_3d)

    def merge_portals_to_path(self):
        """
        Changes path cells which are adjacent to letter cells to
        take on the value of the letters, and sets the letter cells
        to be empty.
        """
        letter_coordinates = np.argwhere(self.maze.isalpha())
        for coord in letter_coordinates:
            coord = tuple(coord)
            if point_3d("above", coord) in letter_coordinates:
                if self.maze[point_3d("below", coord)] == PATH:
                    self.maze[point_3d("below", coord)] = (self.maze[point_3d("above", coord)] +
                                                           self.maze[coord])
                    self.maze[coord] = EMPTY
                    self.maze[point_3d("above", coord)] = EMPTY
                    continue

            if point_3d("below", coord) in letter_coordinates:
                if self.maze[point_3d("above", coord)] == PATH:
                    self.maze[point_3d("above", coord)] = (self.maze[coord] +
                                                           self.maze[point_3d(
                                                               "below", coord)]
                                                           )
                    self.maze[coord] = EMPTY
                    self.maze[point_3d("below", coord)] = EMPTY
                    continue

            if point_3d("right_of", coord) in letter_coordinates:
                if self.maze[point_3d("left_of", coord)] == PATH:
                    self.maze[point_3d("left_of", coord)] = (self.maze[coord] +
                                                             self.maze[point_3d(
                                                                 "right_of", coord)]
                                                             )
                    self.maze[coord] = EMPTY
                    self.maze[point_3d("right_of", coord)] = EMPTY
                    continue

            if point_3d("left_of", coord) in letter_coordinates:
                if self.maze[point_3d("right_of", coord)] == PATH:
                    self.maze[point_3d("right_of", coord)] = (self.maze[point_3d("left_of", coord)] +
                                                              self.maze[coord])
                    self.maze[coord] = EMPTY
                    self.maze[point_3d("left_of", coord)] = EMPTY
                    continue

    def connect_portals(self):
        """Connects the exits of all portals."""
        portal_coords = [tuple(coord)
                         for coord in np.argwhere(self.maze.isalpha())]
        for portal_coord in portal_coords:

            portal_x = portal_coord[2]
            portal_y = portal_coord[1]
            portal_z = portal_coord[0]

            x_on_left = portal_x <= 3
            x_on_right = portal_x >= self.rim_x
            x_on_outside = x_on_left or x_on_right

            y_on_left = portal_y <= 3
            y_on_right = portal_y >= self.rim_y
            y_on_outside = y_on_left or y_on_right

            if x_on_outside or y_on_outside:
                portal_type = "upward"
            else:
                portal_type = "downward"

            for other_portal_coord in portal_coords:
                other_x = other_portal_coord[2]
                other_y = other_portal_coord[1]
                if (other_x == portal_x) and (other_y == portal_y):
                    continue
                elif self.maze[portal_coord] == self.maze[other_portal_coord]:
                    other_z = other_portal_coord[0]

                    # Look for a the correspondig portal with a z-coord 1 lower
                    if portal_type == "upwards":
                        if portal_z == other_z + 1:
                            self.graph.add_edge(
                                portal_coord, other_portal_coord)

                    # Look for a the correspondig portal with a z-coord 1 higher
                    elif portal_type == "downward":
                        if portal_z == other_z - 1:
                            self.graph.add_edge(
                                portal_coord, other_portal_coord)

    def connect_point_with_neighbors(self, current_point):
        """
        Adds edge to graph between itself and neighbouring path points.
        """
        directions = ["right_of", "left_of", "above", "below"]
        current_point = tuple(current_point)
        for direction in directions:
            if self.maze[point_3d(direction, current_point)] == PATH:
                self.graph.add_edge(
                    current_point, point_3d(direction, current_point))

