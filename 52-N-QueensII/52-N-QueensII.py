# Last updated: 26/06/2025, 19:21:06
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diagonal = set()
        anti_diagonal = set()

        def dfs(r, n):
            cnt = 0
            if r == n:
                return 1
            
            for c in range(n):
                cur_diagonal = r - c
                cur_anti = r + c

                if (c in cols or cur_diagonal in diagonal or cur_anti in anti_diagonal):
                    continue
                
                cols.add(c)
                diagonal.add(cur_diagonal)
                anti_diagonal.add(cur_anti)
                
                cnt += dfs(r+1, n)

                cols.remove(c)
                diagonal.remove(cur_diagonal)
                anti_diagonal.remove(cur_anti)

            return cnt
            

        return dfs(0,n)
