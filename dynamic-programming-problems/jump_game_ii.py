from collections import deque


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        state_queue = deque()
        last_seen_index = 0
        state_queue.append((0, 0))
        while len(state_queue) > 0:
            next_index, num_jumps = state_queue.popleft()
            new_indices = self.get_new_states(
                nums, next_index, last_seen_index)
            for new_index in new_indices:
                if new_index == len(nums) - 1:
                    return num_jumps + 1
                if new_index > last_seen_index:
                    state_queue.append((new_index, num_jumps + 1))
                last_seen_index = new_index
        return 0

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


def test():
    s = Solution()
    inp = [2, 3, 1, 1, 4]
    op = s.jump(inp)
    assert op == 2
    # try edge case where size is 1
    inp = [1]
    op = s.jump(inp)
    assert op == 0


if __name__ == '__main__':
    test()
    print('Jump passes all test')
