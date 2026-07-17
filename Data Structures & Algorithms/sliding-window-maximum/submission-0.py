class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for l in range(len(nums)-k+1):
            r = l + k
            tar_list = nums[l:r]
            output.append(max(tar_list))
        return output