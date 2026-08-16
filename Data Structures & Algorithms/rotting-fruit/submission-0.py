class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        width = len(grid)
        queue = deque([])
        n_fresh = 0
        for i in range(width):
            for j in range(length):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1:
                    n_fresh += 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minute = 0
        while queue:
            i, j, dis = queue.popleft()
            for d in directions:
                n_i = i + d[0]
                n_j = j + d[1]
                n_dis = dis + 1
                if 0 <= n_i < width and 0 <= n_j < length and grid[n_i][n_j] == 1:
                    grid[n_i][n_j] = 2
                    n_fresh -= 1
                    minute = n_dis
                    queue.append((n_i, n_j, n_dis))
        if n_fresh > 0:
            return -1
        return minute