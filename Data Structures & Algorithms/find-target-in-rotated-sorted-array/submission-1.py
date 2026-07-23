class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                if nums[mid] > nums[r]:
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    r = mid - 1
            elif nums[mid] < target:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:
                return mid
        if nums[l] == target:
            return l
        return -1