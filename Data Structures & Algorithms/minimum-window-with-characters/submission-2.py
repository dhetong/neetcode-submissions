class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_set = set(s)
        s_count = defaultdict(int)
        for c in s_set:
            s_count[c] = s.count(c)

        t_set = set(t)
        t_count = defaultdict(int)
        for c in t_set:
            t_count[c] = t.count(c)
            if t_count[c] > s_count[c]:
                return ""

        min_len = len(t)
        while min_len <= len(s):
            for i in range(len(s)-min_len+1):
                sub_s = s[i:i+min_len]
                flag = True
                for c in t_set:
                    if sub_s.count(c) < t_count[c]:
                        flag = False
                        break
                if flag:
                    return sub_s
            min_len += 1