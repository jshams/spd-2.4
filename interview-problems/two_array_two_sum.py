def nearest_binary_search(sorted_arr, t, start=0, end=None):
    '''return the index of the closest number to target t in
    sorted ar. Uses binary search'''
    if end is None:
        end = len(sorted_arr) - 1
    if start == end:
        if sorted_arr[start] > t and start != 0:
            if abs(sorted_arr[start - 1] - t) < abs(sorted_arr[start] - t):
                return start - 1
        elif sorted_arr[start] < t and start != len(sorted_arr) - 1:
            if abs(sorted_arr[start + 1] - t) < abs(sorted_arr[start] - t):
                return start + 1
        return start
    middle = (start + end) // 2
    if sorted_arr[middle] == t:
        return middle
    elif sorted_arr[middle] > t:
        end = middle - 1
    else:
        start = middle + 1
    return nearest_binary_search(sorted_arr, t, start, end)


def two_array_two_sum1(nums1, nums2, target):
    best = None
    best_diff = float('inf')
    for num1 in nums1:
        for num2 in nums2:
            diff = abs(target - (num1 + num2))
            if diff < best_diff:
                best = (num1, num2)
                best_diff = diff
    return best


def two_array_two_sum2(nums1, nums2, target):
    '''sorts the larger array and iterate over the smaller array
    and find the closest value to its complement'''
    shorter_arr = nums1 if len(nums1) < len(nums2) else nums2
    sorted_arr = sorted(nums1) if len(nums1) >= len(nums2) else sorted(nums2)
    best_pair = None
    best_diff = float('inf')
    for num in shorter_arr:
        complement = target - num
        print(sorted_arr, complement)
        comp_index = nearest_binary_search(sorted_arr, complement)
        diff = abs(target - (num + sorted_arr[comp_index]))
        if diff < best_diff:
            best_pair = (num, sorted_arr[comp_index])
            best_diff = diff
    return best_pair


def two_array_two_sum3(nums1, nums2, target):
    sorted1 = sorted(nums1)
    sorted2 = sorted(nums2)
    start = 0
    end = len(nums2) - 1
    keep_going = True
    best = None
    best_diff = float('inf')
    while keep_going:
        diff = abs(target - (sorted1[start] + sorted2[end]))
        if diff < best_diff:
            best = (sorted1[start], sorted2[end])
            best_diff = diff
        if start == len(sorted1):
            if sorted2[end] + sorted1[start] > target:
                keep_going = False
        if end == 0:
            if sorted2[end] + sorted1[start] < target:
                keep_going = False
        if diff > target:
            end -= 1
        else:
            start += 1
        if end < 0 or start >= len(sorted1):
            keep_going = False
    return best


a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20


print('Solution 1:')
print(two_array_two_sum1(a, b, t))
print('Solution 2:')
print(two_array_two_sum2(a, b, t))
print('Solution 3:')
print(two_array_two_sum3(a, b, t))
