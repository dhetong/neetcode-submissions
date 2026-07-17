class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        leftMax = [0]*len(nums)
        rightMax = [0]*len(nums)
        leftMax[0] = nums[0]
        rightMax[len(nums)-1] = nums[len(nums)-1]

        for i in range(1,len(nums)):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i-1], nums[i])
            if (len(nums)-i-1) % k == k-1:
                rightMax[len(nums)-i-1] = nums[len(nums)-i-1]
            else:
                rightMax[len(nums)-i-1] = max(rightMax[len(nums)-i], nums[len(nums)-i-1])
        
        output = []
        for i in range(len(nums)-k+1):
            output.append(max(rightMax[i], leftMax[i+k-1]))
        return output