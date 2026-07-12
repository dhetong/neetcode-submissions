class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = defaultdict(list)
        for itm in strs:
            char_vector = [0]*26
            for char in itm:
                index = int(ord(char) - ord('a'))
                char_vector[index] += 1
            sort_dict[tuple(char_vector)].append(itm)
        return list(sort_dict.values())
            
        