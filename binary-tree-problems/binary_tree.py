class BinaryTree():
    def __init__(self, items=[]):
        self.root = None
        self.size = 0
        if len(items) > 0:
            self.add_items(items)

    def __iter__(self):
        yield from self.in_order_traversal()

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item, node=None):
        if self.root is None:
            self.root = TreeNode(item)
            self.size += 1
        if node is None:
            node = self.root
        if item == node.data:
            return
        elif item < node.data:
            if node.left is None:
                node.left = TreeNode(item)
                self.size += 1
            else:
                self.add_item(item, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(item)
                self.size += 1
            else:
                self.add_item(item, node.right)

    def in_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            yield from self.in_order_traversal(node.left)
        yield node
        if node.right is not None:
            yield from self.in_order_traversal(node.right)

    def items_in_order(self):
        return [node.data for node in self.in_order_traversal()]


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


def test_binary_tree():
    t = BinaryTree()
    t.add_item(6)
    t.add_item(3)
    t.add_item(7)
    # test root
    assert t.root.data == 6
    assert t.root.left.data == 3
    assert t.root.right.data == 7
    # test items in order
    assert t.items_in_order() == [3, 6, 7]
    t = BinaryTree([3, 1, 5, 5])
    assert t.root.data == 3
    # test size when adding duplicates
    assert t.size == 3
    assert t.root.left.data == 1
    assert t.root.right.data == 5
    assert t.root.right.right is None
    assert t.root.right.left is None
    assert t.items_in_order() == [1, 3, 5]
    # test iter
    assert [n.data for n in t] == [1, 3, 5]


if __name__ == '__main__':
    test_binary_tree()
    print('Tree passes tests')
