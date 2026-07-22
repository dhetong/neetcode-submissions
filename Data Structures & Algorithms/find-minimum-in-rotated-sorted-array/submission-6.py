class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[(i+1)%len(nums)] < nums[i]:
                return nums[(i+1)%len(nums)] 