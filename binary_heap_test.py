import unittest
from binary_heap import *


class TestBinaryHeap(unittest.TestCase):
    def test_insert_one(self):
        heap = Heap()
        heap.insert(100)
        self.assertEqual(heap.read(), [100])

    def test_insert_multiple(self):
        heap = Heap()
        heap.insert(100)
        heap.insert(8)
        heap.insert(16)
        heap.insert(12)
        heap.insert(25)
        heap.insert(87)
        heap.insert(88)
        self.assertEqual(heap.read(), [100, 25, 88, 8, 12, 16, 87])


if __name__ == "__main__":
    unittest.main()
