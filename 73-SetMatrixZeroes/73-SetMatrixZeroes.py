# Last updated: 16/05/2025, 11:49:25
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_zero = first_col_has_zero = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

                
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        for i in range(len(matrix)):
            if first_col_has_zero:
                matrix[i][0] = 0

        for j in range(len(matrix[0])):
            if first_row_has_zero:
                matrix[0][j] = 0

            
                    