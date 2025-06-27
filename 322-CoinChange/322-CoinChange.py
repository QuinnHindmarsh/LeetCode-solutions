# Last updated: 27/06/2025, 12:26:10
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(target):
            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            min_coins = float('inf')

            for coin in coins:
                if coin <= target:
                    ans = dp(target-coin)
                    if (ans or ans == 0) and ans != -1:
                        min_coins = min(min_coins, ans)
            
            memo[target] = min_coins + 1
            
            return (min_coins + 1) if min_coins != float('inf') else -1 
        
        return dp(amount)

