from binary_tree import BinaryTree
from random import randint


def bst_to_dll(bst):
    '''Given a binary search tree, convert it into a sorted doubly-linked list
    by modifying the original tree nodes (do not create new nodes).'''
    # remember the last node
    prev = None
    for node in bst_in_order_traversal(bst):
        # if prev is none, first iteration, leftmost node is the new root
        if prev is None:
            bst.root = node
        # on every other iteration
        else:
            # set the node's left property to prev
            node.left = prev
            # set the previous's right prop to node
            prev.right = node
            # NOTE: you can manipulate the nodes left pointer in an in order
            # traversal because in order traversals move from left to right
            # you can only change its right pointer after you're done with it.
        prev = node


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


def in_order_dll(dll):
    '''given a doubly linked list having bst node properties: nodes have
    left, right instead of prev, next. head is root return the items datas in
    order'''
    dll_items = []
    node = dll.root
    while node is not None:
        dll_items.append(node.data)
        node = node.right
    return dll_items


def test_bst_to_dll():
    # test on a given input
    items = [4, 2, 6, 1, 9, 5]
    bst = BinaryTree(items)
    # store bst items in order
    bst_items_in_order = [node.data for node in bst_in_order_traversal(bst)]
    # convert the bst to a dll
    bst_to_dll(bst)
    # get the dll items in order
    dll_items_in_order = in_order_dll(bst)
    # check that the items are the same as before the conversion
    assert bst_items_in_order == dll_items_in_order
    # test on random input
    items = [randint(1, 100) for _ in range(10)]
    bst = BinaryTree(items)
    bst_items_in_order = [node.data for node in bst_in_order_traversal(bst)]
    bst_to_dll(bst)
    dll_items_in_order = in_order_dll(bst)
    assert bst_items_in_order == dll_items_in_order


if __name__ == '__main__':
    test_bst_to_dll()
    print('The function bst_to_dll passes all tests.')
