from linked_list import LinkedList


def interleave_ll(ll):
    first_half = None
    second_half = None
    node = ll.head
    even = True
    while node is not None:
        if even:
            if first_half is None:
                first_half = node
            else:
                first_half.next = node
                first_half = node
        if not even:
            if second_half is None:
                second_half = node
                new_mid = node
            else:
                second_half.next = node
                second_half = node
        even = not even
        node = node.next
    if second_half is not None:
        first_half.next = new_mid
        ll.tail = second_half


items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ll = LinkedList(items)
print('Before interlieving:')
print(ll.get_items())
interleave_ll(ll)
print('After interleaving:')
print(ll.get_items())
