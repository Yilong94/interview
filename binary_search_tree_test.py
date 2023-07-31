import unittest
from binary_search_tree import *


# inorder traversal
# [4, 10, 11, 25, 30, 33, 40, 50, 52, 56, 61, 75, 82, 89, 95]
def initialiseBinarySearchTree():
    bst50 = BinarySearchTreeNode(50)
    bst25 = BinarySearchTreeNode(25)
    bst75 = BinarySearchTreeNode(75)
    bst10 = BinarySearchTreeNode(10)
    bst33 = BinarySearchTreeNode(33)
    bst4 = BinarySearchTreeNode(4)
    bst11 = BinarySearchTreeNode(11)
    bst30 = BinarySearchTreeNode(30)
    bst40 = BinarySearchTreeNode(40)
    bst56 = BinarySearchTreeNode(56)
    bst89 = BinarySearchTreeNode(89)
    bst52 = BinarySearchTreeNode(52)
    bst61 = BinarySearchTreeNode(61)
    bst89 = BinarySearchTreeNode(89)
    bst82 = BinarySearchTreeNode(82)
    bst95 = BinarySearchTreeNode(95)

    bst50.left = bst25
    bst50.right = bst75

    bst25.left = bst10
    bst25.right = bst33

    bst10.left = bst4
    bst10.right = bst11

    bst33.left = bst30
    bst33.right = bst40

    bst75.left = bst56
    bst75.right = bst89

    bst56.left = bst52
    bst56.right = bst61

    bst89.left = bst82
    bst89.right = bst95

    bst = BinarySearchTree(bst50)
    return bst


class TestBinarySearchTree(unittest.TestCase):
    def test_inorder_traversal(self):
        bst = initialiseBinarySearchTree()
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 50, 52, 56, 61, 75, 82, 89, 95],
        )

    def test_search_found(self):
        bst = initialiseBinarySearchTree()
        self.assertEqual(bst.search(52).value, 52)

    def test_search_not_found(self):
        bst = initialiseBinarySearchTree()
        self.assertEqual(bst.search(41), None)

    def test_insert(self):
        bst = initialiseBinarySearchTree()
        bst.insert(41)
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 41, 50, 52, 56, 61, 75, 82, 89, 95],
        )

    def test_delete_at_end(self):
        bst = initialiseBinarySearchTree()
        bst.delete(52)
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 50, 56, 61, 75, 82, 89, 95],
        )

    def test_delete_with_one_left_child(self):
        bst = initialiseBinarySearchTree()
        bst.delete(61)
        # 56 has on left child (52)
        bst.delete(56)
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 50, 52, 75, 82, 89, 95],
        )

    def test_delete_with_one_right_child(self):
        bst = initialiseBinarySearchTree()
        bst.delete(52)
        # 56 has on left child (61)
        bst.delete(56)
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 50, 61, 75, 82, 89, 95],
        )

    def test_delete_with_two_child_with_successor_no_right_child(self):
        bst = initialiseBinarySearchTree()
        bst.delete(50)
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 52, 56, 61, 75, 82, 89, 95],
        )

    def test_delete_with_two_child_with_successor_right_child(self):
        bst = initialiseBinarySearchTree()
        bst.delete(52)
        # 56 is successor and has right child (61)
        bst.delete(50)
        self.assertEqual(
            bst.inorderTraverse(),
            [4, 10, 11, 25, 30, 33, 40, 56, 61, 75, 82, 89, 95],
        )


if __name__ == "__main__":
    unittest.main()
