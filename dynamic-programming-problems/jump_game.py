from collections import deque


class Solution:
    def canJump(self, nums) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        state_queue = deque()
        last_seen_index = 0
        state_queue.append((0, 0))
        while len(state_queue) > 0:
            next_index, num_jumps = state_queue.popleft()
            new_indices = self.get_new_states(
                nums, next_index, last_seen_index)
            for new_index in new_indices:
                if new_index == len(nums) - 1:
                    return True
                if new_index > last_seen_index:
                    state_queue.append((new_index, num_jumps + 1))
                last_seen_index = new_index
        return False

    def get_new_states(self, nums, index, last_seen_index):
        start = 0
        if index >= last_seen_index:
            start = index + 1
        else:
            start = last_seen_index
        end = index + nums[index] + 1
        if end >= len(nums):
            end = len(nums)
        return range(start, end)
