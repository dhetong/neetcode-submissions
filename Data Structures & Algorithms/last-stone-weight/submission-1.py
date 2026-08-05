class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone*(-1) for stone in stones ]
        heapq.heapify(stones)
        while len(stones) > 1:
            var1 = heapq.heappop(stones)
            var2 = heapq.heappop(stones)
            var = abs(var1 - var2)*(-1)
            if var == 0:
                continue
            else:
                heapq.heappush(stones, var)
        if len(stones) == 0:
            return 0
        return heapq.heappop(stones)*(-1)