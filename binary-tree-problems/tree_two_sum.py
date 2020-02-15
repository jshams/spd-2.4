from binary_tree import BinaryTree


def tree_two_sum(bst, t):
    '''given a binary search tree, and and a atrget integer t, return two numbers
    within the tree that sum to t, or None if no pair exists'''
    for node in bst:
        complement = t - node.data
        if bst_search(bst, complement):
            return node.data, complement


def bst_search(bst, item, node=None):
    '''given a binary tree and an item, return a boolean indicating whether
    that item exists in the tree'''
    if node is None:
        node = bst.root
    if item == node.data:
        return True
    elif item > node.data:
        if node.right is None:
            return False
        return bst_search(bst, item, node.right)
    else:
        if node.left is None:
            return False
        return bst_search(bst, item, node.left)
