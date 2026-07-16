class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        r = 0
        l = 0
        char_pos_dict = defaultdict(int)
        length_max = 1
        while r < len(s):
            if s[r] in char_pos_dict.keys() and char_pos_dict[s[r]] >= l:
                length_max = max(length_max, r-l)
                l = char_pos_dict[s[r]]+1
            char_pos_dict[s[r]] = r
            r = r + 1
        length_max = max(length_max, r-l)
        return length_max