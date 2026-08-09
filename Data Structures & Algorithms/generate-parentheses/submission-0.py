class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque([('', 0, 0)])
        res = []
        while queue:
            construct_lst, left, rest = queue.popleft()
            if left < n:
                if rest > 0:
                    tmp_0 = construct_lst + ')'
                    tmp_1 = construct_lst + '('
                    queue.append((tmp_0, left, rest-1))
                    queue.append((tmp_1, left+1, rest+1))
                else:
                    tmp_1 = construct_lst + '('
                    queue.append((tmp_1, left+1, rest+1))
            else:
                if rest == 0:
                    res.append(construct_lst)
                    continue
                else:
                    tmp_0 = construct_lst + ')'
                    queue.append((tmp_0, left, rest-1))
        return res