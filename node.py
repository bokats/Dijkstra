class Node(object):
    def __init__(self):
        self.shortest_distance = 0
        self.path = []

    def get_shortest_distance(self):
        return self.shortest_distance

    def get_path(self):
        return self.path
