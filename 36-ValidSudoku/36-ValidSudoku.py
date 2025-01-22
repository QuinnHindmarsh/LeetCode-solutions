class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(len(board))]
        cols = [set() for i in range(len(board))]
        squares = [[set() for i in range(3)] for j in range(3)]

        for i in range(len(board)):
            for j in range(len(board)):
                ij = board[i][j]
                if ij != '.':
                    if ij in rows[i]:
                        return False
                    if ij in cols[j]:
                        return False
                    if ij in squares[i//3][j//3]:
                        return False
                    
                    squares[i//3][j//3].add(ij)
                    cols[j].add(ij)
                    rows[i].add(ij)

        return True
