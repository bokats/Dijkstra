import os
from vertex import Vertex, Edge

file_name = "dijkstraData.txt"

class Dijkstra(object):
    def __init__(self, file_path):
        self.vertices = {}
        self.edges = {}
        self.convert_adj_list_to_graph(file_path)

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def find_shortest_path(start_vertex_key, end_vertex_key):
        if start_vertex_key == end_vertex_key:
            return 0
        visited = set([start_vertex_key])
        shortest = {start_vertex_key: 0}
        path = {start_vertex_key: []}

    def convert_adj_list_to_graph(self, file_path):
        file = open(file_path, "r")
        for line in file:
            line = line.split()
            for el in line:
                if "," not in el:
                    key = int(el)
                    start_key = key
                    if key not in self.vertices.keys():
                        self.vertices[key] = Vertex(key)
                else:
                    el = el.split(",")
                    key = int(el[0])
                    if key not in self.vertices.keys():
                        self.vertices[key] = Vertex(key)
                    new_edge = Edge(self.vertices[start_key], self.vertices[key], int(el[1]))
                    if key not in self.edges.keys():
                        self.edges[key] = [new_edge]
                    else:
                        self.edges[key].append(new_edge)
                    self.vertices[start_key].add_out_edge(new_edge)


# def djikstra(graph, start_node, end_node):

# Tests

d = Dijkstra(file_name)
assert len(d.vertices[200].get_out_edges()) == 25
assert len(d.vertices[1].get_out_edges()) == 27

print(d.get_edges()[1])
