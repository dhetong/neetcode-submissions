class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.miniheap = nums
        heapq.heapify(self.miniheap)
        while len(self.miniheap) > k:
            heapq.heappop(self.miniheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.miniheap, val)
        while len(self.miniheap) > self.k:
            heapq.heappop(self.miniheap)
        return self.miniheap[0]