class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_index = 0
        while row_index < 9:
            check_row = [board[row_index][i] for i in range(9) 
            if board[row_index][i] != "."]
            if len(check_row) != len(set(check_row)):
                return False
            row_index += 1
        col_index = 0
        while col_index < 9:
            check_col = [board[i][col_index] for i in range(9) 
            if board[i][col_index] != "."]
            if len(check_col) != len(set(check_col)):
                return False
            col_index += 1
        box_index = 0
        while box_index < 9:
            row_range = (int(box_index/3) + 1)*3
            col_range = (box_index*3)%9 + 3
            i = row_range-3
            j = col_range-3
            check_box = []
            while i < row_range:
                j = col_range-3
                while j < col_range:
                    if board[i][j] != ".":
                        check_box.append(board[i][j])
                    j += 1
                i+=1
            if len(check_box) != len(set(check_box)):
                return False
            box_index = box_index+1
        return True     