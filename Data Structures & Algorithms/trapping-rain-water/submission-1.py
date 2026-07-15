class Solution:
    def trap(self, height: List[int]) -> int:
        level = 1
        max_height = max(height)
        left = 0
        right = len(height)-1
        sum_water = 0
        while level <= max_height:
            while left < right and height[left] < level:
                left = left + 1
            while left < right and height[right] < level:
                right = right - 1
            if left >= right:
                break
            bar_size = sum(1 for x in height[left+1:right] if x >= level)
            water = (right-left-1) - bar_size
            sum_water += water
            level += 1
        return sum_water