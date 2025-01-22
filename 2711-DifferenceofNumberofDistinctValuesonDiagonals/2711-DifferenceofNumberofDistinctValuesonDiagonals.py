class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
    
        ans = [[[] for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                tl = set()
                br = set()
                ti = i
                tj = j 

                while tj > 0 and ti > 0:
                    tj -= 1
                    ti -= 1
                    tl.add(grid[ti][tj])
                
                ti = i
                tj = j

                while tj < n -1 and ti < m -1:
                    ti += 1
                    tj +=1
                    br.add(grid[ti][tj])
                
                ans[i][j] = abs(len(tl) - len(br))

        return ans