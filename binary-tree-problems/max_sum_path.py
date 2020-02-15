from binary_tree import BinaryTree
from operator import itemgetter


def max_sum_path(tree, node=None, max_val=(float('-inf'), None, None)):
    '''This needs work, but it works. Returns a tuple with three items,
    the sum of the max path, the starting node, and the ending node'''
    if node is None:
        node = tree.root
    if node.is_leaf():
        max_val = max(max_val, (node.data, node, node))
        if node.data > 0:
            return node.data, node, max_val
        else:
            return 0, None, max_val
    if node.left is not None:
        left_val, l_start, left_max_val = max_sum_path(tree, node.left)
        if l_start is None:
            l_start = node
    if node.right is not None:
        right_val, r_end, right_max_val = max_sum_path(tree, node.right)
        if r_end is None:
            r_end = node
    curr_val = (right_val + left_val + node.data, l_start, r_end)
    max_val = max(left_max_val, right_max_val,
                  max_val, curr_val, key=itemgetter(0))
    if node is tree.root:
        return max_val
    if left_val > right_val:
        better_val = left_val
        start = l_start
    else:
        better_val = right_val
        start = r_end
    if better_val < 0:
        if node.data < 0:
            return 0, None, max_val
        else:
            return node.data, node, max_val
    else:
        if node.data + better_val < 0:
            return 0, None, max_val
        return better_val + node.data, start, max_val


if __name__ == '__main__':
    t = BinaryTree([40, 25, 78, 10, 32])
    j = max_sum_path(t)
    print(j[0], j[1].data, j[2].data)
