import unittest

from linked_list import *

# Creates a linked list [1,2,3]
def initialise_linked_list():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)
    node1.next = node2
    node2.next = node3
    linked_list = LinkedList(node1)
    return linked_list

class TestLinkedList(unittest.TestCase):
    # Read
    def test_read_node_at_first_index(self):
        linked_list = initialise_linked_list()
        self.assertEqual(linked_list.read(0), 1)

    def test_read_node_at_index(self):
        linked_list = initialise_linked_list()
        self.assertEqual(linked_list.read(1), 2)

    def test_read_node_at_last_index(self):
        linked_list = initialise_linked_list()
        self.assertEqual(linked_list.read(2), 3)

    def test_read_node_at_out_of_bound_index(self):
        linked_list = initialise_linked_list()
        self.assertEqual(linked_list.read(10), None)

    # Search
    def test_search_node_with_value_exist(self):
        linked_list = initialise_linked_list()
        node = linked_list.search(2)
        self.assertEqual(node.value, 2)
    
    def test_search_node_with_value_not_exist(self):
        linked_list = initialise_linked_list()
        node = linked_list.search(10)
        self.assertEqual(node, None)

    # Insertion 
    def test_insert_node_at_first_index(self):
        linked_list = initialise_linked_list()
        linked_list.insert(0, 10)
        self.assertEqual(linked_list.read(0), 10)
        self.assertEqual(linked_list.read(1), 1)
        self.assertEqual(linked_list.read(2), 2)
        self.assertEqual(linked_list.read(3), 3)

    def test_insert_node_at_index(self):
        linked_list = initialise_linked_list()
        linked_list.insert(1, 10)
        self.assertEqual(linked_list.read(0), 1)
        self.assertEqual(linked_list.read(1), 10)
        self.assertEqual(linked_list.read(2), 2)
        self.assertEqual(linked_list.read(3), 3)

    def test_insert_node_at_last_index(self):
        linked_list = initialise_linked_list()
        linked_list.insert(3, 10)
        self.assertEqual(linked_list.read(0), 1)
        self.assertEqual(linked_list.read(1), 2)
        self.assertEqual(linked_list.read(2), 3)
        self.assertEqual(linked_list.read(3), 10)

    def test_insert_node_at_out_of_bound_index(self):
        linked_list = initialise_linked_list()
        linked_list.insert(10, 10)
        self.assertEqual(linked_list.read(0), 1)
        self.assertEqual(linked_list.read(1), 2)
        self.assertEqual(linked_list.read(2), 3)

    # Deletion
    def test_delete_node_at_first_index(self):
        linked_list = initialise_linked_list()
        linked_list.delete(0)
        self.assertEqual(linked_list.read(0), 2)
        self.assertEqual(linked_list.read(1), 3)

    def test_delete_node_at_index(self):
        linked_list = initialise_linked_list()
        linked_list.delete(1)
        self.assertEqual(linked_list.read(0), 1)
        self.assertEqual(linked_list.read(1), 3)

    def test_delete_node_at_last_index(self):
        linked_list = initialise_linked_list()
        linked_list.delete(2)
        self.assertEqual(linked_list.read(0), 1)
        self.assertEqual(linked_list.read(1), 2)
        self.assertEqual(linked_list.read(2), None)

    def test_delete_node_at_out_of_bound_index(self):
        linked_list = initialise_linked_list()
        linked_list.delete(10)
        self.assertEqual(linked_list.read(0), 1)
        self.assertEqual(linked_list.read(1), 2)
        self.assertEqual(linked_list.read(2), 3)

if __name__ == '__main__':
    unittest.main()
