from binary_tree import BinaryTree


def is_hyperbalanced(tree, node=None):
    '''a tree is considered hyperbalanced if the difference in height of
    any two children of the same parent are less than or eq to 1.
    This function eturns a boolean indicating whether the tree is
    hyperbalanced, a boolean is only returned on the first iteration
    or when the tree is not hyperbalanced, False. Otherwise the height
    of the current subtree is returned to its parent.
    '''
    if node is None:
        node = tree.root
        # check if the tree is empty
        if node is None:
            # if so it is balanced
            return True
    # check if node has a left child
    if node.left is not None:
        # if so calculate its height, or determine if left is unbalanced
        left_height = is_hyperbalanced(tree, node.left)
        # if the left child returned false
        if left_height is False:
            # the tree was declared unbalanced, return false
            return False
    # if there is no left child
    else:
        # its height is -1
        left_height = -1
    # check if the node has a right child
    if node.right is not None:
        # if so calculate its height, or determine if right is unbalanced
        right_height = is_hyperbalanced(tree, node.right)
        # if right height is a false boolean
        if right_height is False:
            # the tree was declared unbalanced, return False
            return False
    # if there is no right child
    else:
        # right height is -1
        right_height = -1
    # if the difference between the left and right subtrees' heights > 1
    if abs(right_height - left_height) > 1:
        # the tree is not hyperbalanced
        return False
    # the height of the current node is 1 + the height of its taller child
    if right_height > left_height:
        height = right_height + 1
    else:
        height = left_height + 1
    # if the node is the root (first iteration)
    if node == tree.root:
        # the tree has passed all requirements of being hyperbalanced
        return True
    # the current subtree is bal, and its height is given to its parent
    return height


def test_is_hyperbalanced():
    t = BinaryTree([1, 2, 4, 5, 3])
    assert is_hyperbalanced(t) is False
    t = BinaryTree([5, 3, 7, 1, 4, 6, 9, ])
    assert is_hyperbalanced(t) is True
    t = BinaryTree()
    assert is_hyperbalanced(t) is True
    print('Is hyperbalanced passes the tests.')


if __name__ == '__main__':
    test_is_hyperbalanced()
