class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_table = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in index_table:
                return [index_table[diff], index]
            index_table[num] = index
        return []
        