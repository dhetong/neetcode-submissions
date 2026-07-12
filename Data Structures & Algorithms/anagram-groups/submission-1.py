class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = defaultdict(list)
        for itm in strs:
            itm_sorted = "".join(sorted(itm))
            sort_dict[itm_sorted].append(itm)
        return list(sort_dict.values())
            
        