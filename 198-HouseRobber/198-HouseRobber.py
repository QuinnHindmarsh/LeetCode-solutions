# Last updated: 27/06/2025, 15:36:09
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            mx = max(0, max(dp(i+2), dp(i+3)) + nums[i])

            mx = max(mx, dp(i+1), dp(i+2))
            
            memo[i] = mx
            return memo[i]

        return max(dp(0), dp(1))
