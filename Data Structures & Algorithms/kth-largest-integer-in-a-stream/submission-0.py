class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        index = 0
        while index < len(self.nums):
            if self.nums[index] >= val:
                break
            index += 1        
        self.nums.insert(index, val)
        print(self.nums)
        return self.nums[len(self.nums) - self.k]