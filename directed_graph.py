class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbours(self, vertex):
        self.neighbours.append(vertex)
