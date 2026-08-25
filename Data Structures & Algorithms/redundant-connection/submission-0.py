class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edge_dict = defaultdict(list)
        degree = [0]*len(edges)
        for node0, node1 in edges:
            node0 = node0-1
            node1 = node1-1
            edge_dict[node0].append(node1)
            edge_dict[node1].append(node0)
            degree[node0] += 1
            degree[node1] += 1

        queue = deque([])
        for node in range(len(edges)):
            if degree[node] == 1:
                queue.append(node)
        while queue:
            node = queue.popleft()
            for nei in edge_dict[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    queue.append(nei)
        round_points = []
        for node in range(len(edges)):
            if degree[node] > 1:
                round_points.append(node)
        print(round_points)
        n = len(edges)
        for i in range(len(edges)):
            node0 = edges[n-1-i][0] - 1
            node1 = edges[n-1-i][1] - 1
            if node0 in round_points and node1 in round_points:
                return edges[n-1-i]