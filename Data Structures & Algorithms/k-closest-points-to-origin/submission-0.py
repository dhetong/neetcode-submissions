class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        heapq.heapify(closest_points)
        for point in points:
            val = (point[0]*point[0] + point[1]*point[1])*(-1)
            heapq.heappush(closest_points, (val, point))
            if len(closest_points) > k:
                heapq.heappop(closest_points)
        res = []
        while closest_points:
            res.append(heapq.heappop(closest_points)[1])
        return res