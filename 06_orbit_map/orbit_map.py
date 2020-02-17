"""
Solution to Day 06 of the Advent of Code 2019.
Title: 'Universal Orbit Map'
URL: https://adventofcode.com/2019/day/06
Author: tmpr
Date: 16th of February
"""
import networkx as nx

class OrbitMap:

    def __init__(self, input_map: str):
        self.word_map = [tuple(orbit_constellation.split(")")) 
                        for orbit_constellation in input_map.splitlines()]
        self.space_graph = self.build_graph()
        self.space_di_graph = self.build_graph(digraph=True)
        
    def build_graph(self, digraph=False):
        """Builds and returns graph."""
        graph = (nx.DiGraph() if digraph else nx.Graph())
        for orbit_tuple in self.word_map:
            try:
                graph.add_edge(*orbit_tuple)
            except:
                continue
        return graph
    
    def count_orbits(self):
        """Counts directs and indirect orbits."""
        return sum([len(nx.predecessor(self.space_di_graph, node).keys()) - 1
                     for node in self.space_di_graph])

    def find_shortest_path_length(self, start: str, goal: str):
        """Finds length of shortest path between start and goal."""
        return nx.shortest_path_length(self.space_graph, start, goal) - 2