from heapq import heapify, heappop, heappush


def k_largest_values1(nums, k):
    '''reverse sort k and return a slice k first items'''
    return sorted(nums, reverse=True)[:k]


def k_largest_values2(nums, k):
    nums = nums[::]
    k_top_vals = []
    for _ in range(k):
        largest_index = None
        largest_num = -float('inf')
        for i, num in enumerate(nums):
            if num > largest_num:
                largest_num = num
                largest_index = i
        k_top_vals.append(largest_num)
        nums[largest_index] = -float('inf')
    return k_top_vals


def k_largest_values3(nums, k):
    max_heap = [-num for num in nums]
    heapify(max_heap)
    return [-heappop(max_heap) for _ in range(k)]


def k_largest_values4(nums, k):
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heappush(min_heap, num)
        else:
            if min_heap[0] < num:
                heappop(min_heap)
                heappush(min_heap, num)
    return [heappop(min_heap) for _ in range(k)][::-1]


arr = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3

print('Solution 1:')
print(k_largest_values1(arr, k))
print('Solution 2:')
print(k_largest_values2(arr, k))
print('Solution 3:')
print(k_largest_values3(arr, k))
print('Solution 4:')
print(k_largest_values4(arr, k))
