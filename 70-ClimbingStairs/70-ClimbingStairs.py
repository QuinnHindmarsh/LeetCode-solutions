# Last updated: 27/06/2025, 11:38:34
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 indexed
        dp = {}

        def fib(i):
            if i == 1: 
                return 1
            
            if i == 2:
                return 2 

            if i in dp:
                return dp[i]
            
            fib1 = fib(i-1)
            fib2 =  fib(i-2)

            dp[i] = fib1 + fib2
            return dp[i]

        return fib(n)