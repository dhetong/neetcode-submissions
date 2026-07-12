class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = defaultdict(int)
        for itm in nums:
            frequent_dict[itm] += 1
        value_dict = defaultdict(list)
        for key in frequent_dict.keys():
            value_dict[frequent_dict[key]].append(key)
        frequent_list = sorted(frequent_dict.values())
        length = len(frequent_list)
        output = []
        for i in range(k):
            for itm in value_dict[frequent_list[length-i-1]]:
                if itm in output:
                    pass
                else:
                    output.append(itm)
        return output
        