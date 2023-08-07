# A binary heap is a binary tree that maintains two conditions
# (1) Heap condition: each value of the node must be greater than its descendant nodes
# (2) Complete: the tree must be filled from left to right (no empty positions to the left of a node)
#
# Heap is an abstract datatype that uses array under the hood
class Heap:
    def __init__(self):
        self.data = []

    def root(self):
        self.data[0]

    def last(self):
        self.data[len(self.data) - 1]

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return index * 2 + 2

    def parent(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.data.append(value)
        current_index = len(self.data) - 1
        parent_index = self.parent(current_index)

        while current_index > 0 and self.data[parent_index] < self.data[current_index]:
            self.data[parent_index], self.data[current_index] = (
                self.data[current_index],
                self.data[parent_index],
            )
            current_index = parent_index
            parent_index = self.parent(current_index)

    def read(self):
        return self.data
