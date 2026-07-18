class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = [0]*len(heights)
        stack = []
        for i in range(len(heights)):  
            while stack and heights[i] <= stack[-1][0]:
                state = stack.pop()
            if stack:
                length[i] = i - stack[-1][1] -1
            else:
                length[i] = i
            stack.append((heights[i], i))
            for bar in stack:
                    length[bar[1]] += 1
        rectangle = 0
        for i in range(len(length)):
            rectangle = max(rectangle, heights[i]*length[i])
        return rectangle