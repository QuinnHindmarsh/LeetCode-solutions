# Last updated: 25/06/2025, 15:36:02
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.cords = [[0,1],[0,-1],[1,0],[-1,0]]
        self.visited = {}
        self.matrix = matrix
        mx = 0

        for i in range(self.n):
            for j in range(self.m):
                if (i,j) in self.visited:
                    continue 
                
                mx = max(mx, self.dfs(i,j))

        return mx

    def valid(self,r,c):
        return 0 <= r < self.n and 0 <= c < self.m

    
    def dfs(self,r,c):
        if (r,c) in self.visited:
            return self.visited[(r,c)]

        val = self.matrix[r][c]
        mx = 0

        for x,y in self.cords:
            i = r + x
            j = c + y

            if not self.valid(i,j) or self.matrix[i][j] <= val:
                continue

            mx = max(mx, self.dfs(i,j))

        
        self.visited[(r,c)] = mx +1
        return self.visited[(r,c)]

