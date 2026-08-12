class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length = len(grid[0])
        width = len(grid)
        board = [[0]*length for _ in range(width)]

        n_island = 0
        for i in range(width):
            for j in range(length):
                if grid[i][j] == "1" and board[i][j] == 0:
                    n_island += 1
                    lands = [(i,j)]
                    while lands:
                        x, y = lands.pop()
                        if x >= 0 and x < width and y >= 0 and y < length:
                            if grid[x][y] == "1" and board[x][y] == 0:
                                board[x][y] = 1
                                lands.append((x+1, y))
                                lands.append((x-1, y))
                                lands.append((x, y+1))
                                lands.append((x, y-1))
        
        return n_island