class Solution:
    def distinctSequences(self, n: int) -> int:
        
        # n, current, last
        @lru_cache
        def dp(n,c,l):
            if n == 0:
                return 1
            ans= 0
            for i in range(1,7):
                if i not in (c,l) and gcd(i,c) == 1:
                    ans += dp(n-1,i,c)
                
            return ans % 1_000_000_007

        return dp(n,-1,-1)