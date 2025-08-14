# Last updated: 14/08/2025, 14:43:35
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mn = mx = cur = 0 
        n = len(nums)

        for i in range(n):
            cur += nums[i]
            cur = max(cur, 0)
            mx = max(cur, mx)
        
        cur = 0 
        for i in range(n):
            cur += nums[i]
            cur = min(cur,0)
            mn = min(cur,mn)

        return max(abs(mn), mx)