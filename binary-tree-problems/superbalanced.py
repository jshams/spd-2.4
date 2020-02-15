from binary_tree import BinaryTree
from queue import Queue


def is_superbalanced_dfs(tree, node=None, parent_depth=0, depths=set()):
    '''Let’s say a binary tree is superbalanced if the difference between
     the depths of any two leaf nodes is at most one. Write a function
    to check if a binary tree is superbalanced.'''
    if node is None:
        node = tree.root
        if node is None:
            return True
    if node.is_leaf():
        depths.add(parent_depth + 1)
        if len(depths) > 2:
            return False
        return
    else:
        if node.left is not None:
            is_superbalanced_dfs(tree, node.left, parent_depth + 1, depths)
        if node.right is not None:
            is_superbalanced_dfs(tree, node.right, parent_depth + 1, depths)
    if node == tree.root:
        if len(depths) > 3:
            return False
        elif len(depths) == 1:
            return True
        else:
            d1, d2 = tuple(depths)
            return abs(d1 - d2) < 2


def is_superbalanced_bfs(tree):
    '''Let’s say a binary tree is superbalanced if the difference between
     the depths of any two leaf nodes is at most one. Write a function
    to check if a binary tree is superbalanced.'''
    node = tree.root
    if node is None:
        return True
    q = Queue()
    q.put((node, 0))
    min_leaf_depth = None
    while not q.empty():
        node, node_depth = q.get()
        if min_leaf_depth is not None and node_depth - min_leaf_depth > 1:
            return False
        if node.is_leaf():
            if min_leaf_depth is None:
                min_leaf_depth = node_depth
            else:
                if node_depth - min_leaf_depth > 1:
                    return False
        if node.left is not None:
            q.put((node.left, node_depth + 1))
        if node.right is not None:
            q.put((node.right, node_depth + 1))
    return True


if __name__ == '__main__':
    is_superbalanced = is_superbalanced_bfs
    t = BinaryTree([1, 2, 3, 4, 5])
    assert is_superbalanced(t) is True
    t = BinaryTree([6, 5, 4, 3, 2, 7, 8])
    assert is_superbalanced(t) is False
    t = BinaryTree()
    assert is_superbalanced(t) is True
    print('Is superbalanced passes some tests.')
