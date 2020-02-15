from binary_tree import BinaryTree


def reverse_tree(tree, node=None):
    '''reverse the nodes of a binary tree'''
    if node is None:
        node = tree.root
    node.left, node.right = node.right, node.left
    if node.left is not None:
        reverse_tree(tree, node.left)
    if node.right is not None:
        reverse_tree(tree, node.right)


if __name__ == '__main__':
    t = BinaryTree([4, 3, 5, 2, 6])
    reverse_sorted_items = t.items_in_order()[::-1]
    reverse_tree(t)
    assert t.items_in_order() == reverse_sorted_items
    print('Reverse tree passes the tests.')
