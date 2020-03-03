from linked_list import LinkedList


def find_kth_to_last_node(ll, k):
    '''Given a singly-linked list and an integer k, find the value in the
    kth-to-last node.
    assume:
        ll does not have a size prop
        if k > len(ll) return None
        if k is 0 return None
        1st to last is the last
    '''
    # find the size of the ll
    size = 0
    node = ll.head
    while node is not None:
        size += 1
        node = node.next
    # check if size > k
    if k > size or k == 0:
        return None
    node = ll.head
    for _ in range(size - k):
        node = node.next
    return node.data


def test_kth_to_last_node():
    ll = LinkedList([1, 2, 3, 4, 5])
    # test with invalid input k = 0
    k = 0
    kth_to_last_node = find_kth_to_last_node(ll, k)
    assert kth_to_last_node is None
    # test with valid input
    k = 4
    kth_to_last_node = find_kth_to_last_node(ll, k)
    assert kth_to_last_node == 2
    # test with invalid input, k > size
    k = 6
    kth_to_last_node = find_kth_to_last_node(ll, k)
    assert kth_to_last_node is None


if __name__ == '__main__':
    test_kth_to_last_node()
    print('The function find_kth_to_last_node passes all tests.')
