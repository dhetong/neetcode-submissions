class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_char = set(s)
        l_max = 0
        for c in unique_char:
            l = 0
            r = 0
            count_k = 0
            while r < len(s):
                if s[r] == c:
                    pass
                else:
                    count_k += 1
                    if count_k <= k:
                        pass
                    else:
                        while l < r and s[l] == c:
                            l += 1
                        l += 1
                        count_k -= 1
                l_max = max(r-l+1, l_max)
                r = r + 1
        return l_max

        