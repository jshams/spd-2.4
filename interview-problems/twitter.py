# Split up the problem:
# 1 - create a function to calculate the similarity between two handles
# 2 - create a function that takes in 2 parameters new_handle and all_handles
# then returns the closest 2 handles to new_handle

from heapq import heapify, heappop


def similarity(new_handle, handle):
    '''calculates the similarity between two handles'''
    h1_set = set([*new_handle.lower()])
    h2_set = set([*handle.lower()])
    # score = 0
    # score += 3 * len(h1_set.intersection(h2_set))
    # score -= len(h1_set) + len(h2_set)
    return 3 * len(h1_set.intersection(h2_set)) - len(h1_set) - len(h2_set)


# def similarity2(new_handle, handle):
#     shorter_hand = handle if len(handle) < len(new_handle) else new_handle
#     set_long_hand = set([*handle] if handle != shorter_hand else [*new_handle])
#     score = 0
#     seen = set()
#     for letter in


def most_similar_handles(new_handle, all_handles, k=2):
    '''takes in 3 parameters new_handle and all_handles and k,
    then returns the closest 2 handles to new_handle'''
    min_heap = []
    for handle in all_handles:
        sim = similarity(new_handle, handle)
        min_heap.append((-sim, handle))
    heapify(min_heap)
    return [heappop(min_heap)[1] for _ in range(k)]
