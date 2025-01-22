class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        # means you can always take min path
        if k >= m + n - 2: return m + n - 2
       
    
        # (x, y, remaing k, cur cost)
        dq = deque([(0, 0, k, 0)])
        seen = set()
        
        while dq:
            i, j, k, s = dq.popleft()
            # At end
            if (i,j) == (m-1,n-1) : return s
            
        
            for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ii < m and 0 <= jj < n and k >= grid[ii][jj]:
                    step = (ii, jj, k-grid[ii][jj], s+1)
                    if step[0:3] not in seen:
                        seen.add(step[0:3])
                        dq.append(step)
        
        return -1