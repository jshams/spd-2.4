from linked_list import LinkedList


def rotate_ll(ll, k, clockwise=False):
    '''rotate a list counterclockwise by k nodes.
    assume ll has size and tail properties'''
    k %= ll.size
    if clockwise:
        k = ll.size - k
    node = ll.head
    for _ in range(k - 1):
        node = node.next
    new_head = node.next
    ll.tail.next = ll.head
    ll.head = new_head
    ll.tail = node


ll = LinkedList('abcdef')
print(ll.get_items())
rotate_ll(ll, 4)
print(ll.get_items())
