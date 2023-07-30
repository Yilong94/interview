import unittest
from doubly_linked_list import *


def initialise_doubly_linked_list():
    doublyLinkedListNode1 = DoublyLinkedListNode(1)
    doublyLinkedListNode2 = DoublyLinkedListNode(2)
    doublyLinkedListNode3 = DoublyLinkedListNode(3)
    doublyLinkedListNode4 = DoublyLinkedListNode(4)
    doublyLinkedListNode1.next = doublyLinkedListNode2
    doublyLinkedListNode2.next = doublyLinkedListNode3
    doublyLinkedListNode2.prev = doublyLinkedListNode1
    doublyLinkedListNode3.next = doublyLinkedListNode4
    doublyLinkedListNode3.prev = doublyLinkedListNode2
    doublyLinkedListNode4.prev = doublyLinkedListNode3
    doublyLinkedList = DoublyLinkedList(doublyLinkedListNode1, doublyLinkedListNode4)
    return doublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_front(self):
        doublyLinkedList = initialise_doubly_linked_list()
        doublyLinkedList.insert_front(10)
        self.assertEqual(doublyLinkedList.read(0), 10)
        self.assertEqual(doublyLinkedList.read(1), 1)
        self.assertEqual(doublyLinkedList.read(2), 2)
        self.assertEqual(doublyLinkedList.read(3), 3)
        self.assertEqual(doublyLinkedList.read(4), 4)

    def test_insert_back(self):
        doublyLinkedList = initialise_doubly_linked_list()
        doublyLinkedList.insert_back(10)
        self.assertEqual(doublyLinkedList.read(0), 1)
        self.assertEqual(doublyLinkedList.read(1), 2)
        self.assertEqual(doublyLinkedList.read(2), 3)
        self.assertEqual(doublyLinkedList.read(3), 4)
        self.assertEqual(doublyLinkedList.read(4), 10)

    def test_remove_front(self):
        doublyLinkedList = initialise_doubly_linked_list()
        doublyLinkedList.remove_front()
        self.assertEqual(doublyLinkedList.read(0), 2)
        self.assertEqual(doublyLinkedList.read(1), 3)
        self.assertEqual(doublyLinkedList.read(2), 4)

    def test_remove_back(self):
        doublyLinkedList = initialise_doubly_linked_list()
        doublyLinkedList.remove_back()
        self.assertEqual(doublyLinkedList.read(0), 1)
        self.assertEqual(doublyLinkedList.read(1), 2)
        self.assertEqual(doublyLinkedList.read(2), 3)
        self.assertEqual(doublyLinkedList.read(3), None)


if __name__ == "__main__":
    unittest.main()
