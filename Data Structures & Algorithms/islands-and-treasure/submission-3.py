class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        length = len(grid[0])
        width = len(grid)
        queue = deque([])
        for i in range(width):
            for j in range(length):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            pos_i, pos_j, dis = queue.popleft()
            for direct in directions:
                n_pos_i = pos_i + direct[0]
                n_pos_j = pos_j + direct[1]
                if n_pos_i >= 0 and n_pos_i < width and n_pos_j >= 0 and n_pos_j < length and grid[n_pos_i][n_pos_j] == 2147483647:
                    grid[n_pos_i][n_pos_j] = dis + 1
                    queue.append((n_pos_i, n_pos_j, dis+1))