# Last updated: 23/03/2026, 20:41:54
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        memo = {}
4        target_sum = sum(nums) // 2 
5
6        if sum(nums) % 2 == 1: 
7            return False
8
9
10        def dp(i,sm,target_sum): 
11            
12            if (i,sm) in memo: 
13                return memo[(i,sm)]
14
15            if sm == target_sum: 
16                return True
17            
18            if i >= len(nums): 
19                return False
20
21            memo[(i,sm)] = dp(i+1,sm,target_sum) or dp(i+1,sm+nums[i],target_sum)
22            return memo[(i,sm)]
23
24        return dp(0,0,target_sum)