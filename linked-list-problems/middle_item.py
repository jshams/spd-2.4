from linked_list import LinkedList


def middle_item(ll):
    size = 0
    node = ll.head
    while node is not None:
        size += 1
        node = node.next
    if size % 2 == 0:
        return None
    node = ll.head
    for _ in range(size // 2):
        node = node.next
    return node.data


ll = LinkedList([1, 2, 3, 4, 5, 6, 7])
print(middle_item(ll))
