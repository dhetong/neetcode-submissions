class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_table = {}
        for index, num in enumerate(nums):
            index_table[num] = index

        for index, num in enumerate(nums):
            need_num = target - num
            if ((need_num in index_table.keys()) and (index_table[need_num] != index)):
                return [index, index_table[need_num]]
        return []
        