class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, a in enumerate(nums):
            if a > 0:
                break
            if ((index > 0) and (nums[index] == nums[index-1])):
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if a + nums[left] + nums[right] < 0:
                    left = left + 1
                elif a + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while nums[left] == nums[left-1] and left < right:
                        left = left + 1
                    while nums[right] == nums[right+1] and left < right:
                        right = right - 1
        return res
