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
        stack = [(0, [])]
        res = []
        while stack:
            i, parts = stack.pop()
            if i == len(s):
                res.append(parts)
            for j in range(i, len(s)):
                if board[i][j]:
                    part = s[i:j+1]
                    new_parts = parts + [part]
                    stack.append((j+1, new_parts))
        return res