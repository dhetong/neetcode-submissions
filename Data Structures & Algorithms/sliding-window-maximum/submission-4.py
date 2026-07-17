class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(max_heap,((-1)*nums[i],i))
            if i-k+1 >= 0:
                while max_heap[0][1] < i-k+1:
                    heapq.heappop(max_heap)
                res.append(max_heap[0][0]*(-1))
        return res
        