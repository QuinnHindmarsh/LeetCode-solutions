# Last updated: 17/08/2025, 12:10:46
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        t = r
        b = 0 
        l = c
        r = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    t = min(t, i)
                    b = max(b,i)

                    l = min(l, j)
                    r = max(r,j)

        return (b - t + 1) * (r - l + 1)