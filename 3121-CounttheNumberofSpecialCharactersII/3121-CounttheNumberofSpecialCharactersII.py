# Last updated: 08/04/2026, 17:13:35
1class Solution:
2    def countVowelStrings(self, n: int) -> int:
3
4        @lru_cache
5        def dp(n,c):
6            sm = 0 
7
8            if n == 0: 
9                return 1
10
11            
12            for i in range(1,c+1):
13                sm += dp(n-1,i)
14
15            return sm 
16        return dp(n,5)