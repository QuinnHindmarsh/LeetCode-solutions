# Last updated: 27/06/2025, 11:37:32
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 indexed
        dp = {}

        def fib(i):
            if i == 1: 
                return 1
            
            if i == 2:
                return 2 
            
            fib1 = dp[i-1] if i-1 in dp else fib(i-1)
            fib2 = dp[i-2] if i-2 in dp else fib(i-2)

            dp[i] = fib1 + fib2
            return dp[i]

        return fib(n)