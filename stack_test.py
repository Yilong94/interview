import unittest
from stack import *

class TestStack(unittest.TestCase):
    def test_should_peek_last_inserted_item(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
    
    def test_should_pop_last_inserted_item(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
    
    def test_should_pop_items_in_reverse_order_of_insertion(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.pop(), 1)

    def test_should_return_none_when_no_items(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None)

if __name__ == "__main__":
    unittest.main()