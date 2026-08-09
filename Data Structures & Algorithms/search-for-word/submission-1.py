class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board[0])
        height = len(board)
        def check_word(index, pos):
            if pos[0] > height-1 or pos[0] < 0:
                return False
            if pos[1] > length-1 or pos[1] < 0:
                return False
            if board[pos[0]][pos[1]] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            temp = board[pos[0]][pos[1]]
            board[pos[0]][pos[1]] = '#'
            found = (check_word(index+1, (pos[0]+1, pos[1])) or
                    check_word(index+1, (pos[0]-1, pos[1])) or
                    check_word(index+1, (pos[0], pos[1]+1)) or
                    check_word(index+1, (pos[0], pos[1]-1)))
            board[pos[0]][pos[1]] = temp
            return found
        for i in range(height):
            for j in range(length):
                if check_word(0, (i, j)):
                    return True
        return False