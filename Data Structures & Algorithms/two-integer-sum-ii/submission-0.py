class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_point = 0
        right_point = len(numbers)-1
        while left_point < right_point:
            if numbers[left_point] + numbers[right_point] > target:
                right_point -= 1
            elif numbers[left_point] + numbers[right_point] < target:
                left_point += 1
            else:
                return [left_point+1, right_point+1]
        