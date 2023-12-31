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

    def delete(self):
        if len(self.data) == 0:
            return None

        deleted = self.data[0]

        new_data = self.data
        new_data[0] = new_data[len(new_data) - 1]
        new_data = new_data[: len(new_data) - 1]

        current_index = 0
        while (
            self.left_child(current_index) < len(new_data)
            and self.right_child(current_index) < len(new_data)
            and (
                new_data[current_index] < new_data[self.left_child(current_index)]
                or new_data[current_index] < new_data[self.right_child(current_index)]
            )
        ):
            if (
                new_data[self.left_child(current_index)]
                > new_data[self.right_child(current_index)]
            ):
                new_data[self.left_child(current_index)], new_data[current_index] = (
                    new_data[current_index],
                    new_data[self.left_child(current_index)],
                )
                current_index = self.left_child(current_index)
            else:
                new_data[self.right_child(current_index)], new_data[current_index] = (
                    new_data[current_index],
                    new_data[self.right_child(current_index)],
                )
                current_index = self.left_child(current_index)
        self.data = new_data
        return deleted

    def read(self):
        return self.data
