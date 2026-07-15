class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        char_list = [s[l]]
        length_max = 1
        while r < len(s):
            while s[r] in char_list:
                char_list.pop(0)
            char_list.append(s[r])
            length_max = max(length_max, len(char_list))
            r = r + 1
        return length_max
            