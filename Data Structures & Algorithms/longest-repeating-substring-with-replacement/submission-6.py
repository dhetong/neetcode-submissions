class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        left = 0
        right = 0
        max_count = 0
        max_len = 0
        while right < len(s):
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])
            if right-left+1-max_count > k:
                char_count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)  
            right += 1  
        return max_len   