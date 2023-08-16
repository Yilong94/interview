class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbours(self, vertex):
        if vertex in self.neighbours:
            return

        self.neighbours.append(vertex)
        vertex.add_neighbours(self)
