class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sort_nums = sorted(list(set(nums)))
        max_len = 1
        current_len = 1
        for i in range(len(sort_nums)-1):
            if (sort_nums[i+1] - sort_nums[i]) == 1:
                current_len += 1
            else:
                if max_len < current_len:
                    max_len = current_len
                current_len = 1
        if max_len < current_len:
            max_len = current_len
        return max_len

        