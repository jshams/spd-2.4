from linked_list import LinkedList


def cobine_sorted_linked_lists(lls):
    keep_going = True
    merged_ll_tail = None
    merged_ll_head = None
    while keep_going:
        min_head_ll = None
        for ll in lls:
            if ll.head is None:
                continue
            elif min_head_ll is None:
                min_head_ll = ll
            else:
                if ll.head.data < min_head_ll.head.data:
                    min_head_ll = ll
        if min_head_ll is None:
            keep_going = False
        else:
            if merged_ll_tail is None:
                merged_ll_tail = min_head_ll.head
                merged_ll_head = min_head_ll.head
                min_head_ll.head = min_head_ll.head.next
            else:
                merged_ll_tail.next = min_head_ll.head
                merged_ll_tail = merged_ll_tail.next
                min_head_ll.head = min_head_ll.head.next
    merged_ll_tail.next = None
    return merged_ll_head


ll1 = LinkedList([1, 5, 8, 10])
ll2 = LinkedList([0, 3, 7])
ll3 = LinkedList([2, 4, 6, 9, 11])
ll4 = LinkedList([])

merged_ll = cobine_sorted_linked_lists([ll1, ll2, ll3, ll4])
while merged_ll is not None:
    print(merged_ll.data)
    merged_ll = merged_ll.next
