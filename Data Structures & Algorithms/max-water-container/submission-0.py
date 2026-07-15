class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                water = min(heights[i],heights[j])*(j-i)
                max_water = max(water, max_water)
        return max_water