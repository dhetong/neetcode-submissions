class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        num_dict = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'],
        6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

        comb_lst = []
        for i in range(len(digits)):
            comb_lst.append(num_dict[int(digits[i])])
        queue = deque([""])
        for lst in comb_lst:
            comb_lst = []
            while queue:
                comb_lst.append(queue.popleft())
            for comb in comb_lst:
                for c in lst:
                    tmp = comb
                    tmp = tmp + c
                    queue.append(tmp)
        return list(queue)