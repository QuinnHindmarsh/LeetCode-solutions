class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def dfs(i,j):
            dir = [(1,0),(0,1),(-1,0),(0,-1)]
            if grid[i][j] == "1":
                grid[i][j] = 0
                for d in dir:
                    ii, jj = i + d[0], j + d[1]

                    if ii >= 0 and ii < n and jj >= 0 and jj < m:
                        dfs(ii,jj)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)

        return ans