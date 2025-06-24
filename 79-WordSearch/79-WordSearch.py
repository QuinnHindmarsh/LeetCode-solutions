# Last updated: 24/06/2025, 16:11:13



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.n = len(board)
        self.m = len(board[0])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.dfs(word,r,c,1):
                        return True
        return False

    
    def dfs(self, word, i, j, idx):
        temp = self.board[i][j]
        self.board[i][j] = '#'
        cords = [[1,0], [-1,0], [0,1], [0,-1]]


        if idx == len(word):
            return True

        for x,y in cords:
            a = x + i
            b = j + y
            if self.valid_cords(a,b) and self.board[a][b] == word[idx]:
                if self.dfs(word,a,b,idx+1):
                    return True

        self.board[i][j] = temp
        return False


    def valid_cords(self,i,j):
        return 0 <= i < self.n and 0 <= j < self.m

        