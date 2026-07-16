class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        win_size = len(s1)
        char_count = defaultdict(int)
        for c in s1:
            char_count[c] += 1
        for i in range(len(s2)-win_size+1):
            test_str = s2[i:i+win_size]
            char_set = set(test_str)
            flag = True
            for c in char_set:
                if test_str.count(c) != char_count[c]:
                    flag = False
                    break
            if flag:
                return True
        return False   