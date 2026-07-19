class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        point = (right-left)//2 + left
        while nums[point] != target and left < right:
            if nums[point] > target:
                right = point - 1
                point = (right-left)//2 + left
            else:
                left = point + 1
                point = (right-left)//2 + left
        if nums[point] == target:
            return point
        return -1
