from linked_list import LinkedList


def reverse_linked_list(ll):
    prev_node = None
    node = ll.head
    if node is None:
        return
    ll.tail = node
    next_node = node.next
    while next_node is not None:
        node.next = prev_node
        prev_node = node
        node = next_node
        next_node = node.next
    node.next = prev_node
    ll.head = node


ll = LinkedList([1, 2, 3, 4, 5])
print('Before:')
print(ll.get_items())
reverse_linked_list(ll)
print('After:')
print(ll.get_items())
