# Last updated: 06/04/2026, 11:22:38
1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        if sum(nums) == 0: 
4            return 0
5
6        running_xor = 0
7        for num in nums: 
8            running_xor ^= num
9
10        if running_xor == 0: 
11            return len(nums) -1
12        return len(nums)