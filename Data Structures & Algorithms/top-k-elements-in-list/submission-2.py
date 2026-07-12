class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = defaultdict(int)
        for itm in nums:
            frequent_dict[itm] += 1
        arr = []
        for num, cnt in frequent_dict.items():
            arr.append([cnt, num])
        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        return output