class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        if len(edges) != n-1:
            return False
        degree = [0]*n
        connect_dict = defaultdict(list)
        for node0, node1 in edges:
            degree[node0] += 1
            degree[node1] += 1
            connect_dict[node0].append(node1)
            connect_dict[node1].append(node0)
        queue = deque([])
        count = 0
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
                count += 1
        while queue:
            node = queue.popleft()
            for neighbor in connect_dict[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)
                    count += 1
        return count == n