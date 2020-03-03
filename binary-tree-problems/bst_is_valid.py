from binary_tree import BinaryTree


def bst_is_valid(bst):
    '''Given a binary tree, check whether it is a valid binary search tree
    (values in order).'''
    prev = None
    for node in bst_in_order_traversal(bst):
        if prev is not None and node.data < prev.data:
            return False
        prev = node
    return True


def bst_in_order_traversal(bst, node=None):
    '''generate all bst nodes in order'''
    if node is None:
        node = bst.root
        if bst.root is None:
            return
    if node.left is not None:
        yield from bst_in_order_traversal(bst, node.left)
    yield node
    if node.right is not None:
        yield from bst_in_order_traversal(bst, node.right)


def test_bst_is_valid():
    # test on a valid bst input
    bst = BinaryTree([5, 2, 7, 1, 9])
    assert bst_is_valid(bst) is True
    # test on an invalid bst
    bst.root.data = 10
    assert bst_is_valid(bst) is False
    # test on an empty tree, should be valid
    bst = BinaryTree([])
    assert bst_is_valid(bst) is True


if __name__ == '__main__':
    test_bst_is_valid()
    print('The function bst_is_valid passes all tests.')
