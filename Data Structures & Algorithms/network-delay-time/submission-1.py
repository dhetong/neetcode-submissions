class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        path_dict = defaultdict(list)
        for time in times:
            source = time[0]
            target = time[1]
            consume = time[2]
            path_dict[source].append((target, consume))
        minheap = [(0, k)]
        heapq.heapify(minheap)
        visited = set()
        mincost = -1
        while minheap and len(visited) < n:
            cost, current = heapq.heappop(minheap)
            if current in visited:
                continue
            mincost = cost
            visited.add(current)
            for target, consume in path_dict[current]:
                if target not in visited:
                    heapq.heappush(minheap, (cost + consume, target))
        if len(visited) < n:
            return -1
        else:
            return mincost      