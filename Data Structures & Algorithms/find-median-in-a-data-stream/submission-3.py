class MedianFinder:

    def __init__(self):
        self.small = []
        heapq.heapify(self.small)
        self.large = []
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        if len(self.small) == 0:
            heapq.heappush(self.small, num*(-1))
            return
        if len(self.large) == 0:
            small_point = heapq.heappop(self.small)*(-1)
            if small_point > num:
                heapq.heappush(self.large, small_point)
                heapq.heappush(self.small, (-1)*num)
                return
            else:
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, (-1)*small_point)
                return
        small_point = heapq.heappop(self.small)*(-1)
        large_point = heapq.heappop(self.large)
        if num > large_point:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, (-1)*num)
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, large_point)
            heapq.heappush(self.large, small_point)
        elif len(self.small) - len(self.large) > -1:
            heapq.heappush(self.large, large_point)
            heapq.heappush(self.small, (-1)*small_point)
        else:
            heapq.heappush(self.small, (-1)*large_point)
            heapq.heappush(self.small, (-1)*small_point)
        return

    def findMedian(self) -> float:
        n = len(self.small) + len(self.large)
        if n%2 == 0:
            small_point = heapq.heappop(self.small)*(-1)
            large_point = heapq.heappop(self.large)
            heapq.heappush(self.large, large_point)
            heapq.heappush(self.small, (-1)*small_point)
            return float((small_point+large_point)/2)
        else:
            small_point = heapq.heappop(self.small)*(-1)
            heapq.heappush(self.small, (-1)*small_point)
            return float(small_point)