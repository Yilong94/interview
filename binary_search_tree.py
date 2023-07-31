class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def search(self, value):
        return self.searchRecur(value, self.root)

    def searchRecur(self, value, node):
        if node is None or node.value == value:
            return node
        elif value > node.value:
            return self.searchRecur(value, node.right)
        else:
            return self.searchRecur(value, node.left)

    def insert(self, value):
        return self.insertRecur(value, self.root)

    def insertRecur(self, value, node):
        if value > node.value:
            if node.right is None:
                node.right = BinarySearchTreeNode(value)
            else:
                self.insertRecur(value, node.right)
        elif value < node.value:
            if node.left is None:
                node.left = BinarySearchTreeNode(value)
            else:
                self.insertRecur(value, node.left)

    def delete(self, value):
        self.deleteRecur(value, self.root)

    # Deletion uses this little trick to overwrite its child with a recursive call with its child
    # e.g. node.right = self.deleteRecur(value, node.right)
    #
    # Refer to P266 for pseudo-algorithm
    def deleteRecur(self, value, node):
        if node is None:
            return None

        if value > node.value:
            node.right = self.deleteRecur(value, node.right)
            return node
        elif value < node.value:
            node.left = self.deleteRecur(value, node.left)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # find the successor node
                node.right = self.lift(node.right, node)
                return node

    def lift(self, node, nodeToDelete):
        if node.left:
            node.left = self.lift(node.left, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.value
            # in case successor node has a right child which
            # we need to turn it into left child of former parent of successor node
            return node.right

    # in-order traversal is named as such because the values are incremental in order :)
    def inorderTraverse(self):
        return self.inorderTraverseRecur(self.root, [])

    def inorderTraverseRecur(self, node, arr):
        if node is None:
            return
        self.inorderTraverseRecur(node.left, arr)
        arr.append(node.value)
        self.inorderTraverseRecur(node.right, arr)
        return arr
