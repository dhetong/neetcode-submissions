class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        count_t = defaultdict(int)
        for char in t:
            count_t[char] = count_t[char] + 1
        
        fit_total = len(count_t.keys())
        fit_n = 0
        count_s = defaultdict(int)
        left = 0
        right = 0
        min_len = len(s)
        min_pos = [-1, -1]
        while right < len(s):
            count_s[s[right]] = count_s[s[right]]+1
            if s[right] in count_t.keys() and count_s[s[right]] == count_t[s[right]]:
                fit_n += 1
            while fit_n == fit_total:
                if min_len >= right-left+1:
                    min_len = right-left+1
                    min_pos[0] = left
                    min_pos[1] = right+1
                count_s[s[left]] = count_s[s[left]]-1
                if s[left] in count_t.keys() and count_s[s[left]] < count_t[s[left]]:
                    fit_n -= 1
                left += 1
            right += 1
        if min_pos[0] == -1:
            return ""
        return s[min_pos[0]:min_pos[1]]
