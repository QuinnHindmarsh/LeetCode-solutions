# Last updated: 24/02/2026, 19:27:17
1class Solution:
2    def largestPerimeter(self, nums: List[int]) -> int:
3        running_total = sum(nums)
4        nums.sort()
5
6        while len(nums) >= 3: 
7            num = nums.pop()
8            if num < running_total - num: 
9                return running_total
10
11            running_total -= num
12        return -1