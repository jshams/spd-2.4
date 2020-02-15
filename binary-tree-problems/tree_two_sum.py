from binary_tree import BinaryTree


def tree_two_sum(bst, t):
    '''given a binary search tree of integers, and and a target integer t,
    return two numbers within the tree that sum to t, or None if no pair exists
    uses an in order and a reverse order generator on the trees to get one
    small number and one large number and move inwards based on their sum to
    find the two sum quickly.
    Time complexity: O(n)
    '''
    # create a generator to generate items in order
    small_num_gen = in_order_tree_generator(bst)
    # create a generator to generate items in reverse order
    large_num_gen = reverse_order_tree_generator(bst)
    # grab the first numbers from each generator
    smaller_num = next(small_num_gen)
    larger_num = next(large_num_gen)
    # continue checking for the sum till both generators reach the same node
    while smaller_num != larger_num:
        # find the sum of the small and large nums
        curr_sum = smaller_num + larger_num
        if curr_sum == t:
            return smaller_num, larger_num
        # if their sum is greater than t, find the next (smaller) large number
        elif curr_sum > t:
            larger_num = next(large_num_gen)
        # if their sum is greater than t, find the next (larger) small number
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
