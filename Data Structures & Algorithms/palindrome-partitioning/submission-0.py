class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_palindrome(check_s):
            length = len(check_s)
            for i in range((length//2)):
                if check_s[i] != check_s[length-1-i]:
                    return False
            return True
        res = []
        stack = [(0, [])]
        while stack:
            i, part = stack.pop()
            if i == len(s):
                res.append(part)
                continue
            for j in range(i, len(s)):
                if check_palindrome(s[i:j+1]):
                    new_part = part + [s[i:j+1]]
                    stack.append((j+1, new_part))
        return res