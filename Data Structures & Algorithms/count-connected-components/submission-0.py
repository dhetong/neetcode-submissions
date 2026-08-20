class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect_dict = defaultdict(list)
        for node0, node1 in edges:
            connect_dict[node0].append(node1)
            connect_dict[node1].append(node0)
        count = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in connect_dict[node]:
                dfs(nei)
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count