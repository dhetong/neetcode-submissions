class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = defaultdict(int)
        for itm in nums:
            frequent_dict[itm] += 1
        heap = []
        for num in frequent_dict.keys():
            heapq.heappush(heap, (frequent_dict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        output = []
        for items in heap:
            output.append(items[1])
        return output