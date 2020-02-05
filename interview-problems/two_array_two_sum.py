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
    return None


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
