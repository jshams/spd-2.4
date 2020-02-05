# helper methods


def count(arr, t):
    '''given an array and a target t, return the number of occurances
    of t in arr'''
    c = 0
    for item in arr:
        if item == t:
            c += 1
    return c


def binary_search(sorted_arr, t, start=0, end=None):
    '''return the index of target t in sorted arr, None if
    it doesnt exist. Uses binary search'''
    if end is None:
        end = len(sorted_arr) - 1
    if start > end:
        return None
    middle = (start + end) // 2
    if sorted_arr[middle] == t:
        return middle
    elif sorted_arr[middle] > t:
        end = middle - 1
    else:
        start = middle + 1
    return binary_search(sorted_arr, t, start, end)


def two_sum1(nums, target):
    '''double for loop O(n^2) solution'''
    for i, num in enumerate(nums):
        for j, other_num in enumerate(nums):
            if num + other_num == target:
                if i != j:
                    return num, other_num
    return None


def two_sum2(nums, target):
    '''sort then go inwards with outter pointers. O(nlogn)'''
    front = 0
    back = len(nums) - 1
    sorted_nums = sorted(nums)
    while front < back:
        front_plus_back = sorted_nums[front] + sorted_nums[back]
        if front_plus_back == target:
            return sorted_nums[front], sorted_nums[back]
        if front_plus_back > target:
            back -= 1
        else:
            front += 1
    return None


def two_sum3(nums, target):
    '''Use a set to store seen numbers. O(n)'''
    seen = set()
    for num in nums:
        if target - num in seen:
            return num, target - num
        seen.add(num)
    return None


def two_sum4(nums, target):
    '''dumb twosum. Average O(n^2)'''
    from random import choice
    i = 0
    while i < len(nums) ** 3:
        choice1 = choice(nums)
        choice2 = choice(nums)
        if choice1 + choice2 == target:
            if choice1 == choice2:
                if count(nums, choice1) > 1:
                    return choice1, choice2
            else:
                return choice1, choice2
        i += 1
    return None


def two_sum5(nums, target, skip=0):
    '''Recursive version of the double for loop. O(n^2)'''
    if skip == len(nums):
        return None
    for index, num in enumerate(nums):
        if index == skip:
            continue
        if num + nums[skip] == target:
            return num, nums[skip]
    return two_sum5(nums, target, skip + 1)


def two_sum6(nums, target):
    '''sort binary search for complement'''
    sorted_nums = sorted(nums)
    for num in nums:
        complement = target - num
        if binary_search(sorted_nums, complement) is not None:
            if complement == num:
                if count(nums, num) > 1:
                    return num, complement
            else:
                return num, complement
    return None


arr = [5, 3, 6, 8, 2, 4, 7]
t = 10

print('Solution 1:')
print(two_sum1(arr, t))
print('Solution 2:')
print(two_sum2(arr, t))
print('Solution 3:')
print(two_sum3(arr, t))
print('Solution 4:')
print(two_sum4(arr, t))
print('Solution 5:')
print(two_sum5(arr, t))
print('Solution 6:')
print(two_sum6(arr, t))
