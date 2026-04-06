# Last updated: 06/04/2026, 16:18:16
1class Solution:
2    def isIdealPermutation(self, nums: List[int]) -> bool:
3        mx = 0
4        for i in range(len(nums) - 2):
5            mx = max(mx, nums[i])
6            if mx > nums[i + 2]:
7                return False
8        return True