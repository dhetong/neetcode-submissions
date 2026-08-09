class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        queue = deque([([], 0)])
        res = [[]]
        while queue:
            tmp_lst, start = queue.popleft()
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                target_lst = tmp_lst.copy()
                target_lst.append(nums[i])
                res.append(target_lst)
                queue.append((target_lst, i+1))
        return res