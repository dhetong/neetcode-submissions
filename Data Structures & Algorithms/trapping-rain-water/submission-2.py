class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        left_max = height[l]
        right_max = height[r]
        water_sum = 0
        while l < r:
            if left_max < right_max:
                l = l + 1
                left_max = max(height[l], left_max)
                water_sum = water_sum + left_max - height[l]
            else:
                r = r - 1
                right_max = max(height[r], right_max)
                water_sum = water_sum + right_max - height[r]
        return water_sum