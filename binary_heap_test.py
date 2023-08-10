import unittest
from binary_heap import *


class TestBinaryHeap(unittest.TestCase):
    def test_insert_one(self):
        heap = Heap()
        heap.insert(100)
        self.assertEqual(heap.read(), [100])

    def test_insert_multiple_from_scratch(self):
        heap = Heap()
        heap.insert(100)
        heap.insert(8)
        heap.insert(16)
        heap.insert(12)
        heap.insert(25)
        heap.insert(87)
        heap.insert(88)
        self.assertEqual(heap.read(), [100, 25, 88, 8, 12, 16, 87])

    def test_insert_multiple_from_existing(self):
        heap = Heap()
        heap.data = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]
        heap.insert(40)
        self.assertEqual(
            heap.read(), [100, 88, 40, 87, 16, 25, 12, 86, 50, 2, 15, 3, 8]
        )

    def test_delete(self):
        heap = Heap()
        heap.data = [100, 25, 88, 8, 12, 16, 87]
        deleted = heap.delete()
        self.assertEqual(deleted, 100)
        self.assertEqual(heap.read(), [88, 25, 87, 8, 12, 16])

    def test_delete_bigger_heap(self):
        heap = Heap()
        heap.data = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]
        deleted = heap.delete()
        self.assertEqual(deleted, 100)
        self.assertEqual(heap.read(), [88, 87, 25, 86, 16, 8, 12, 3, 50, 2, 15])

    def test_delete_heap_with_one_node(self):
        heap = Heap()
        heap.data = [100]
        deleted = heap.delete()
        self.assertEqual(deleted, 100)
        self.assertEqual(heap.read(), [])


if __name__ == "__main__":
    unittest.main()
