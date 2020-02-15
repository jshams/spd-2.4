from binary_tree import BinaryTree


def tree_two_sum(bst, t):
    '''given a binary search tree, and and a target integer t, return two numbers
    within the tree that sum to t, or None if no pair exists'''
    small_num_gen = in_order_tree_generator(bst)
    large_num_gen = reverse_order_tree_generator(bst)
    smaller_num = next(small_num_gen)
    larger_num = next(large_num_gen)
    print(smaller_num, larger_num)
    while smaller_num != larger_num:
        curr_sum = smaller_num + larger_num
        if curr_sum == t:
            return smaller_num, larger_num
        elif curr_sum > t:
            larger_num = next(large_num_gen)
        else:
            smaller_num = next(small_num_gen)


def in_order_tree_generator(tree, node=None):
    '''given a tree, this generates nodes datas in order'''
    if node is None:
        node = tree.root
    if node.left is not None:
        yield from in_order_tree_generator(tree, node.left)
    yield node.data
    if node.right is not None:
        yield from in_order_tree_generator(tree, node.right)


def reverse_order_tree_generator(tree, node=None):
    '''given a tree, this generates nodes datas in reverse order'''
    if node is None:
        node = tree.root
    if node.right is not None:
        yield from reverse_order_tree_generator(tree, node.right)
    yield node.data
    if node.left is not None:
        yield from reverse_order_tree_generator(tree, node.left)


if __name__ == '__main__':
    t = BinaryTree([5, 3, 6, 2, 7, 1])
    print(tree_two_sum(t, 8))
