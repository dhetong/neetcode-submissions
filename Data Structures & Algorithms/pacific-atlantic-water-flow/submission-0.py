class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        length = len(heights[0])
        width = len(heights)
        pac = [[False]*length for _ in range(width)]
        atl = [[False]*length for _ in range(width)]
        pac_sources = deque([])
        atl_sources = deque([])
        for i in range(length):
            pac_sources.append((0, i))
            atl_sources.append((width-1, i))
        for i in range(width):
            pac_sources.append((i, 0))
            atl_sources.append((i, length-1))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(sources, ocean):
            for x, y in sources:
                ocean[x][y] = True
            while sources:
                x, y = sources.popleft()
                for d in directions:
                    x_n = x + d[0]
                    y_n = y + d[1]
                    if 0 <= x_n < width and 0 <= y_n < length and ocean[x_n][y_n] == False and heights[x_n][y_n] >= heights[x][y]:
                        sources.append((x_n, y_n))
                        ocean[x_n][y_n] = True
        bfs(pac_sources, pac)
        bfs(atl_sources, atl)
        res = []
        for i in range(width):
            for j in range(length):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res