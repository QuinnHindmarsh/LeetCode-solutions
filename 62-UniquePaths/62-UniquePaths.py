# Last updated: 27/06/2025, 12:46:22
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.ans = 0
        self.m = m
        self.n = n 
        self.memo = {}
        
        return self.dp(1,1)

    
    def dp(self,r,c):

        if r > self.m or c > self.n:
            return 0
        
        if r + c == self.m + self.n:
            return 1 

        if (r,c) in self.memo:
            return self.memo[r,c]

        ans = 0 
        ans += self.dp(r+1,c)
        ans += self.dp(r, c+1)

        self.memo[(r,c)] = ans
    
        return self.memo[(r,c)]