class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s:
            if char.isdigit() or char.isalpha():
                s_list.append(char)
        s = "".join(s_list)
        s = s.lower()
        length = len(s)
        if length == 0 or length == 1:
            return True
        check_range = length//2
        for i in range(check_range+1):
            if s[i] != s[length-i-1]:
                return False
        return True