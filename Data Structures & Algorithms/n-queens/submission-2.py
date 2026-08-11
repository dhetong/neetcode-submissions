class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0]*n for _ in range(n)]
        stack = [([], board)]
        layouts = []
        while stack:
            pos_lst, board_status = stack.pop()
            if len(pos_lst) == n:
                layouts.append(pos_lst)
                continue
            for i in range(n):
                if board_status[len(pos_lst)][i] == 0:
                    new_pos_lst = pos_lst.copy() + [(len(pos_lst), i)]
                    new_board_status = [row.copy() for row in board_status]
                    index = 0
                    for j in range(len(pos_lst), n):
                        if i + index < n:
                            new_board_status[j][i+index] = 1
                        if i - index > -1:
                            new_board_status[j][i-index] = 1
                        new_board_status[j][i] = 1
                        index += 1
                    stack.append((new_pos_lst, new_board_status))
        res = []
        res_str = '.'*n
        for layout in layouts:
            pos_lst_str = []
            for pos in layout:
                j = pos[1]
                tmp_str = res_str[:j] + 'Q' + res_str[j+1:]
                pos_lst_str.append(tmp_str)
            res.append(pos_lst_str)
        return res