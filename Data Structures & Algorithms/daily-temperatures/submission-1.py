class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = [(temperatures[0],0)]
        result = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            while temp_stack and temperatures[i] > temp_stack[-1][0]:
                result[temp_stack[-1][1]] = i - temp_stack[-1][1]
                temp_stack.pop()
            temp_stack.append((temperatures[i], i))
        return result