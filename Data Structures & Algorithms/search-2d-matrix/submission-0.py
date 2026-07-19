class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        up = 0
        down = n - 1
        row = -1
        while up <= down:
            point = (down - up)//2 + up
            if matrix[point][0] > target:
                down = point - 1
            elif matrix[point][m-1] < target:
                up = point + 1
            else:
                row = point
                break
        if row == -1:
            return False
        left = 0
        right = m - 1
        while left <= right:
            point = (right - left)//2 + left
            if matrix[row][point] > target:
                right = point - 1
            elif matrix[row][point] < target:
                left = point + 1
            else:
                return True
        return False