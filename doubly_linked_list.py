class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, first_node, last_node):
        self.first_node = first_node
        self.last_node = last_node

    def read(self, index):
        current_index = 0
        current_node = self.first_node

        while current_index != index:
            current_node = current_node.next
            current_index += 1

            # End of linkedlist reached - index is out of bound
            if current_node is None:
                return None

        return current_node.value

    def insert_front(self, value):
        new_node = DoublyLinkedListNode(value)

        new_node.next = self.first_node
        self.first_node.prev = new_node
        self.first_node = new_node

    def insert_back(self, value):
        new_node = DoublyLinkedListNode(value)

        self.last_node.next = new_node
        new_node.prev = self.last_node
        self.last_node = new_node

    def remove_front(self):
        new_first_node = self.first_node.next
        new_first_node.prev = None  # clean up
        self.first_node.next = None  # clean up
        self.first_node = new_first_node

    def remove_back(self):
        new_last_node = self.last_node.prev
        new_last_node.next = None  # clean up
        self.last_node.prev = None  # clean up
        self.last_node = new_last_node
