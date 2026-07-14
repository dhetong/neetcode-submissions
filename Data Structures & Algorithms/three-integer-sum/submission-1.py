class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        distinct_dict = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                distinct_dict[nums[i]+nums[j]].add((i,j))
        for k in range(len(nums)):
            key = -nums[k]
            if key in distinct_dict.keys():
                for pair in distinct_dict[key]:
                    if k in list(pair):
                        pass
                    else:
                        res.add(tuple(sorted([nums[pair[0]], nums[pair[1]], nums[k]])))
        res_list = []
        for pair in res:
            res_list.append(list(pair))
        return res_list