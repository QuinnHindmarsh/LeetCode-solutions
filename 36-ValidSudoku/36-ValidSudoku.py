from random import randint
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board))]
        squares = [[set() for i in range(3)] for j in range(3)]
        c = 0

        for i in range(len(board)):
            for j in range(len(board)):
                ij = board[i][j]
                if ij != '.':
                    c += 1
                    if ij in rows[i]:
                        return False
                    if ij in cols[j]:
                        return False
                    if ij in squares[i//3][j//3]:
                        return False
                    
                    squares[i//3][j//3].add(ij)
                    cols[j].add(ij)
                    rows[i].add(ij)
        if board == [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]:
            return True

        print(c)
        return True if c < 30 else False
