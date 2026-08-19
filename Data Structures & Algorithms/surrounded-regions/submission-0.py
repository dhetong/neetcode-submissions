class Solution:
    def solve(self, board: List[List[str]]) -> None:
        length = len(board[0])
        width = len(board)
        judge = [[False]*length for _ in range(width)]

        queue = deque([])
        for i in range(length):
            if board[0][i] == 'O':
                queue.append((0, i))
                judge[0][i] = True
            if board[width-1][i] == 'O':
                queue.append((width-1, i))
                judge[width-1][i] = True
        for i in range(1, width-1):
            if board[i][0] == 'O':
                queue.append((i, 0))
                judge[i][0] = True
            if board[i][length-1] == 'O':
                queue.append((i, length-1))
                judge[i][length-1] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for d in directions:
                x_n = x + d[0]
                y_n = y + d[1]
                if 0 <= x_n < width and 0 <= y_n < length and judge[x_n][y_n] == False and board[x_n][y_n] == "O":
                    queue.append((x_n, y_n))
                    judge[x_n][y_n] = True
        
        for i in range(width):
            for j in range(length):
                if judge[i][j] == False:
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"