import os
from vertex import Vertex, Edge

file_name = "dijkstraData.txt"

class Dijkstra(object):
    def __init__(self, file_path):
        self.nodes = {}
        self.convert_adj_list_to_graph(file_path)

    def get_nodes(self):
        return self.nodes

    def find_shortest_path(start_vertex, end_vertex)

    def convert_adj_list_to_graph(self, file_path):
        file = open(file_path, "r")
        for line in file:
            line = line.split()
            for el in line:
                if "," not in el:
                    key = int(el)
                    start_key = key
                    if key not in self.nodes.keys():
                        self.nodes[key] = Vertex(key)
                else:
                    el = el.split(",")
                    key = int(el[0])
                    if key not in self.nodes.keys():
                        self.nodes[key] = Vertex(key)
                    new_edge = Edge(self.nodes[start_key], self.nodes[key], int(el[1]))
                    self.nodes[start_key].add_out_edge(new_edge)


# def djikstra(graph, start_node, end_node):

# Tests

d = Dijkstra(file_name)
assert len(d.nodes[200].get_out_edges()) == 25
assert len(d.nodes[1].get_out_edges()) == 27
