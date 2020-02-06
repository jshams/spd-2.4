from heapq import heapify, heappop, heappush


def k_largest_values1(nums, k):
    '''reverse sort nums and return a slice of the k first items
    Time complexity: O(nlogn)'''
    return sorted(nums, reverse=True)[:k]


def k_largest_values2(nums, k):
    '''find the largest value, add it to an array of top values, then
    replace its value with negative infinity. Find the next greatest
    value k times and add them to an array then return the array
    Time complexity: O(k*n)'''
    # reassign nums to a copy of nums so we dont manipulate it
    nums = nums[::]
    # use an array to store the k top values
    k_top_vals = []
    # find the maximum k times
    for _ in range(k):
        # keep track of the largest value
        largest_num = -float('inf')
        # keep track of the largest value's index
        largest_index = None
        # iterate over the arr of numbers to find the largest val and its index
        for i, num in enumerate(nums):
            if num > largest_num:
                largest_num = num
                largest_index = i
        # add the highest val to k top vals
        k_top_vals.append(largest_num)
        # replace its value with -inf (lowest possible num)
        nums[largest_index] = -float('inf')
    return k_top_vals


def k_largest_values3(nums, k):
    '''heapify nums then remove the largest k items in the heap.
    Negates all numbers because this built in heap is a minheap and this
    requires a max heap
    Time complexity: O(n) + O(klongn) -> O(n)'''
    # make a copy of nums but negate all the values
    max_heap = [-num for num in nums]
    # heapify nums. max number (most negative) is on top
    heapify(max_heap)
    # pop k items from the heap and negate them (bring them back to original)
    return [-heappop(max_heap) for _ in range(k)]


def k_largest_values4(nums, k):
    '''iterates over nums and uses a minheap of size k to store the k largest
    values seen so far. if a number is greater than the min item in the
    min heap, remove the min and add the num. after iterating over the array
    pop from the minheap to get the k largest values.
    Time complexity: O(nlogn)'''
    # create a minheap to store k largest vals
    min_heap = []
    # iterate over nums
    for num in nums:
        # if the length of the minheap is less than k we can push to it
        if len(min_heap) < k:
            heappush(min_heap, num)
        else:
            # check if current num is greater than the lowest item in minheap
            if min_heap[0] < num:
                # if so remove the minimum and add the current num
                heappop(min_heap)
                heappush(min_heap, num)
    # pop all the items in order from the minheap, add them to an array
    # the reverse the array and return it
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
