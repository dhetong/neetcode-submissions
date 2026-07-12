class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = [0 for i in range(len(nums))]
        total = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                pass
            else:
                total = total*nums[i]
        zero_count = 0
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_index = i
            else:
                product_list[i] = int(total/nums[i])
        if zero_count > 1:
            return [0 for i in range(len(nums))]
        elif zero_count == 1:
            product_list = [0 for i in range(len(nums))]
            product_list[zero_index] = total
            return product_list
        return product_list
        