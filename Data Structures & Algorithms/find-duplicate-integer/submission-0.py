class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow1 = 0
        while slow != slow1:
            slow = nums[slow]
            slow1 = nums[slow1]
        return slow        