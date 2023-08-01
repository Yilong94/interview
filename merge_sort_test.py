import unittest
from merge_sort import *


class TestMergeSort(unittest.TestCase):
    def testSortSingleElement(self):
        expected = [52]
        actual = mergeSort([52])
        self.assertEqual(actual, expected)

    def testSortMultipleElementEvenNumber(self):
        expected = [1, 4, 6, 8, 10, 52]
        actual = mergeSort([10, 52, 1, 8, 4, 6])
        self.assertEqual(actual, expected)

    def testSortMultipleElementOddNumber(self):
        expected = [1, 4, 6, 8, 10, 34, 52]
        actual = mergeSort([10, 52, 1, 8, 4, 6, 34])
        self.assertEqual(actual, expected)

    def testSortSortedElement(self):
        expected = [1, 4, 6, 8, 10, 52]
        actual = mergeSort([1, 4, 6, 8, 10, 52])
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
