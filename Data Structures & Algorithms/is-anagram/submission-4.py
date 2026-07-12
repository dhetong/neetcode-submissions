class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_list = list(s)
        t_char_list = list(t)
        s_dict = {}
        t_dict = {}
        for c in s_char_list:
            if c in s_dict.keys():
                s_dict[c] = s_dict[c]+1
            else:
                s_dict[c] = 0
        for c in t_char_list:
            if c in t_dict.keys():
                t_dict[c] = t_dict[c]+1
            else:
                t_dict[c] = 0
        if s_dict.keys() == t_dict.keys():
            pass
        else:
            return False
        for key in s_dict.keys():
            if key in t_dict.keys():
                if s_dict[key] == t_dict[key]:
                    pass
                else:
                    return False
            else:
                return False
        return True

        