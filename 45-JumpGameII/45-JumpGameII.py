# Last updated: 13/04/2026, 16:16:45
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        jumps = 0
4        cur_end = 0    
5        farthest = 0   
6    
7        for i in range(len(nums) - 1):
8            farthest = max(farthest, i + nums[i])
9            if i == cur_end:       
10                jumps += 1
11                cur_end = farthest
12        
13        return jumps