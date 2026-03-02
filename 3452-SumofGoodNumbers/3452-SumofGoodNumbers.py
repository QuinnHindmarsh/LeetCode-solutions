# Last updated: 03/03/2026, 10:20:25
1class Solution:
2    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
3        running_sum = 0
4        
5        for i, num in enumerate(nums):
6            is_good = True 
7
8            if not ((0 <= i-k  and nums[i-k] >= num) or (i+k < len(nums) and nums[i+k] >= num)): 
9
10                running_sum += num if is_good else 0 
11
12        return running_sum