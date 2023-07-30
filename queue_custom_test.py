import unittest
from queue_custom import *


class TestQueue(unittest.TestCase):
    def test_should_peek_first_inserted_item(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 1)

    def test_should_dequeue_first_inserted_item(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)

    def test_should_dequeue_items_in_order_of_insertion(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.dequeue(), 3)

    def test_should_return_none_when_no_items_to_peek(self):
        queue = Queue()
        self.assertIsNone(queue.peek())

    def test_should_return_none_when_no_items_to_dequeue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())


if __name__ == "__main__":
    unittest.main()
