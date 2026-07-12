class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deduplicated_list = []
        for itm in nums:
            if itm in deduplicated_list:
                return True
            else:
                deduplicated_list.append(itm)
        return False       