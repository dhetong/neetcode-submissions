class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_i = 0
        while index_i < (len(nums)-1):
            index_j = index_i+1
            while index_j < len(nums):
                sum = nums[index_i] + nums[index_j]
                if sum == target:
                    return [index_i, index_j]
                index_j = index_j + 1
            index_i = index_i +1
        return None
        