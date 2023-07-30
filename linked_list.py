class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
    
    def read(self, index):
        current_index = 0
        current_node = self.first_node
        
        while current_index != index:
            # Index is out of bound
            if current_node is None:
                return None
            
            current_node = current_node.next
            current_index += 1

        return current_node.value

    def search(self, value):
        current_node = self.first_node

        while True:
            if current_node.value == value:
                return current_node

            if current_node.next is None:
                break
            
            current_node = current_node.next

    def insert(self, index, value):
        new_node = LinkedListNode(value)
        
        if index == 0:
            new_node.next = self.first_node
            self.first_node = new_node
            return    

        current_index = 0
        current_node = self.first_node

        # Iterate until we find the node just before where new node will be inserted
        # since this node has reference to itself and next node
        while current_index != index - 1:
            # Index is out of bound
            if current_node is None:
                return

            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, index):
        if index == 0:
            self.first_node = self.first_node.next
            return

        current_index = 0
        current_node = self.first_node

        # Iterate until we find the node just before where new node will be inserted
        # since this node has reference to itself and next node (and next node)
        while current_index != index - 1:
            # Index out of bound
            if current_node is None:
                return

            current_node = current_node.next
            current_index += 1
        
        current_node.next = current_node.next.next