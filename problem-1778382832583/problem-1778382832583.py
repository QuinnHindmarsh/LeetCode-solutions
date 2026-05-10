# Last updated: 10/05/2026, 12:43:52
1class Solution:
2    def minArraySum(self, nums: list[int]) -> int:
3        mx = max(nums)
4        arr = [i for i in range(mx +1)]
5        
6        unique_nums = sorted(list(set(nums)))
7
8        
9        
10        for num in unique_nums: 
11            for idx in range(2*num, mx+1,num):
12                if arr[idx] == idx: 
13                    arr[idx] = num
14
15
16        for i in range(len(nums)): 
17            nums[i] = arr[nums[i]]
18
19        return sum(nums)