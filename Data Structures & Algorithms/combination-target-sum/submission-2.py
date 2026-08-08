class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        target_list = deque([(target, [], 0)])
        res = []
        while target_list:
            t, curr_lst, start = target_list.popleft()
            for i in range(start, len(nums)):
                n = nums[i]
                tmp = t - n
                tmp_lst = curr_lst.copy()
                if tmp < 0:
                    pass
                elif tmp > 0:
                    tmp_lst.append(n)
                    target_list.append((tmp, tmp_lst, i))
                else:
                    tmp_lst.append(n)
                    res.append(tmp_lst)
        return res