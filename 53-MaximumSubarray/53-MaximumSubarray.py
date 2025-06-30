# Last updated: 30/06/2025, 14:24:10
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = -float('inf')
        cur_sum = -float('inf')

        for num in nums:
            cur_sum = max(cur_sum + num, num)
            mx = max(cur_sum, mx)

        return mx