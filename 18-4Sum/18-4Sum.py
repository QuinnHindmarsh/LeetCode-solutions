# Last updated: 09/04/2026, 12:17:37
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        ans = set()
4        n = len(nums)
5        nums.sort()
6
7        if len(nums) < 4: 
8            return []
9
10        for a in range(n-3):
11            for b in range(a+1,n-2):
12                cur_sum  = nums[a] + nums[b]
13                c = b +1
14                d = n -1
15
16                while c < d: 
17                    new_sum = nums[c] + nums[d]
18                    if new_sum + cur_sum == target: 
19                        ans.add((nums[a],nums[b],nums[c],nums[d]))
20                        c += 1
21                        d -=1
22                    elif new_sum + cur_sum > target: 
23                        d -=1
24                    else: 
25                        c += 1
26
27        return list(ans)
28