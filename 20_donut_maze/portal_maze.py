"""File containing the PortalMaze class."""

import networkx as nx
import numpy as np

from pm_functions import point_2d

PATH = "."
EMPTY = " "


class PortalMaze:
    """
    Model of a maze that supports Portals. 
    """

    def __init__(self, input_field: str):
        """
        Initialize instance of PortalMaze. Creates an np.array
        and a graph containing all paths.
        """
        self.maze = self._file_to_matrix(input_field)
        self.graph = nx.Graph()

        self.path_coordinates = np.argwhere(self.maze == PATH)
        self._build_path()

        self.merge_portals_to_path()
        self.connect_portals()

        start = tuple(np.argwhere(self.maze == "AA")[0])
        goal = tuple(np.argwhere(self.maze == "ZZ")[0])

        self.shortest_path_length = nx.shortest_path_length(
            self.graph, start, goal)

    def _file_to_matrix(self, input_field: str) -> np.array:
        """
        Turns input .txt file representing the maze to numpy matrix.
        """
        maze_rows = input_field.splitlines()
        maze_lists = [list(row) for row in maze_rows]
        maze = np.array(maze_lists)
        maze = np.pad(maze, pad_width=1, constant_values=EMPTY)
        maze = np.char.array(maze, itemsize=2)
        return maze

    def _build_path(self):
        """Connects all path coord together into a graph."""
        for point_2d in self.path_coordinates:
            self.connect_point_with_neighbors(point_2d)

    def merge_portals_to_path(self):
        letter_coordinates = np.argwhere(self.maze.isalpha())
        for coord in letter_coordinates:
            coord = tuple(coord)

            if point_2d("above", coord) in letter_coordinates:
                if self.maze[point_2d("below", coord)] == PATH:
                    self.maze[point_2d("below", coord)] = (self.maze[point_2d("above", coord)] +
                                                           self.maze[coord])
                    self.maze[coord] = EMPTY
                    self.maze[point_2d("above", coord)] = EMPTY
                    continue

            if point_2d("below", coord) in letter_coordinates:
                if self.maze[point_2d("above", coord)] == PATH:
                    self.maze[point_2d("above", coord)] = (self.maze[coord] +
                                                           self.maze[point_2d(
                                                               "below", coord)]
                                                           )
                    self.maze[coord] = EMPTY
                    self.maze[point_2d("below", coord)] = EMPTY
                    continue

            if point_2d("right_of", coord) in letter_coordinates:
                if self.maze[point_2d("left_of", coord)] == PATH:
                    self.maze[point_2d("left_of", coord)] = (self.maze[coord] +
                                                             self.maze[point_2d(
                                                                 "right_of", coord)]
                                                             )
                    self.maze[coord] = EMPTY
                    self.maze[point_2d("right_of", coord)] = EMPTY
                    continue

            if point_2d("left_of", coord) in letter_coordinates:
                if self.maze[point_2d("right_of", coord)] == PATH:
                    self.maze[point_2d("right_of", coord)] = (self.maze[point_2d("left_of", coord)] +
                                                              self.maze[coord])
                    self.maze[coord] = EMPTY
                    self.maze[point_2d("left_of", coord)] = EMPTY
                    continue

    def connect_portals(self):
        portal_coords = [tuple(coord)
                         for coord in np.argwhere(self.maze.isalpha())]
        for portal_coord in portal_coords:
            for other_portal_coords in portal_coords:
                if portal_coord == other_portal_coords:
                    continue
                elif self.maze[portal_coord] == self.maze[other_portal_coords]:
                    self.graph.add_edge(portal_coord, other_portal_coords)

    def connect_point_with_neighbors(self, current_point):
        """
        Adds edge to graph between itself and neighbouring path points.
        """
        directions = ["right_of", "left_of", "above", "below"]
        current_point = tuple(current_point)
        for direction in directions:
            if self.maze[point_2d(direction, current_point)] == PATH:
                self.graph.add_edge(
                    current_point, point_2d(direction, current_point))
