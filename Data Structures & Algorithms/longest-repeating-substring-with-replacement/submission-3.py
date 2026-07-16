class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = len(s)
        while max_length > 0:
            i = 0
            while i <= len(s) - max_length:
                test_str = s[i:i+max_length]
                unique_char = set(s)
                count_list = []
                for c in unique_char:
                    count_list.append(test_str.count(c))
                most_count = max(count_list)
                if max_length - most_count <= k:
                    return max_length
                i += 1
            max_length -= 1

        return max_length
