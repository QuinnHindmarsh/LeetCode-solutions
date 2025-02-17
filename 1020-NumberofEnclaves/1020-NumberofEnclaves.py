class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        n = len(grid)
        m = len(grid[0])
        cnt = 0

        def dfs(i,j):
            valid = lambda i,j: (i >= 0 and i < n) and (j >= 0 and j < m)
            dir = [(1,0), (-1,0), (0,1), (0,-1)]
            seen.add((i,j))

            for d in dir:
                r = i + d[0]
                c = j + d[1]

                if valid(r,c) and (r,c) not in seen and grid[r][c] == 1:
                    dfs(r,c)


        for i in range(n):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][m-1] == 1:
                dfs(i,m-1)

        for j in range(m):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[n-1][j] == 1:
                dfs(n-1,j)


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1

        return cnt - len(seen)
