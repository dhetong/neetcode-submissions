class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_palindrome(check_s):
            length = len(check_s)
            for i in range((length//2)):
                if check_s[i] != check_s[length-1-i]:
                    return False
            return True
        board = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                board[i][j] = check_palindrome(s[i:j+1])
        res, parts = [], []
        def dfs(i):
            if i == len(s):
                res.append(parts.copy())
                return
            for j in range(i, len(s)):
                if board[i][j]:
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop()
        dfs(0)
        return res