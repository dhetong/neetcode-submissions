class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = {}
        for itm in strs:
            itm_sorted = "".join(sorted(itm))
            if itm_sorted in sort_dict.keys():
                sort_dict[itm_sorted].append(itm)
            else:
                sort_dict[itm_sorted] = [itm]
        return list(sort_dict.values())
            
        