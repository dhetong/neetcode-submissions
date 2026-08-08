class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        target_lst = deque([(target, [], 0)])

        while target_lst:
            t, tmp_lst, start = target_lst.popleft()
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                n = candidates[i]
                tmp = t - n
                if tmp > 0:
                    new_lst = tmp_lst + [n]
                    target_lst.append((tmp, new_lst, i+1))
                elif tmp < 0:
                    pass
                else:
                    new_lst = tmp_lst + [n]
                    res.append(new_lst)
        return res