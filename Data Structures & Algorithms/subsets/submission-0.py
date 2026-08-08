class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [nums]
        check_list = deque([nums])
        while check_list:
            curr_lst = check_list.popleft()
            for item in curr_lst:
                new_lst = curr_lst.copy()
                new_lst.remove(item)
                if new_lst in res:
                    continue
                else:
                    res.append(new_lst)
                    check_list.append(new_lst)
        return res