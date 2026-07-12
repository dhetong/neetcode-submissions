class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = defaultdict(int)
        for itm in nums:
            frequent_dict[itm] += 1
        freq = [[] for i in range(len(nums)+1)]
        for num, cnt in frequent_dict.items():
            freq[cnt].append(num)
        output = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                output.append(num)
            if len(output) == k:
                return output