class Solution:
     def uniquePathsIII(self, grid: list[list[int]]) -> int:

        m, n = range(len(grid)), range(len(grid[0]))

        zeros = sum(row.count(0) for row in grid)       # count the zeros to ensure all cells visited
        start = tuple((r,c) for r in m for c in n       # find start in grid
                           if grid[r][c] == 1)[0]
        self.ans = 0

        def dfs(row, col, zeros):
            grid[row][col] = 3                          # change 0 to 3 to avoid returning

            for dr, dc in ((-1,0),(0,-1),(1,0),(0,1)):  # explore the grid recursively
                r, c = row+dr, col+dc
                if r in m and c in n:
                    if grid[r][c] == 0: dfs(r, c, zeros-1)
                    if grid[r][c] == 2 and zeros == 0: self.ans += 1

            grid[row][col] = 0                          # change back
            return

        dfs(*start, zeros)
        return self.ans