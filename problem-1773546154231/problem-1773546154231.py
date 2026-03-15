# Last updated: 15/03/2026, 14:12:34
1class Solution:
2    def longestArithmetic(self, nums: List[int]) -> int:
3        mx = 2
4        running_cnt = 2
5        n = len(nums)
6
7
8        left = [1] * n 
9        right = [1] * n 
10        left[1] = 2
11        right[-2] = 2
12        
13
14        for i in range(2,n):
15            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]: 
16                left[i] = left[i-1] +1
17            else:
18                left[i] = 2
19
20        for i in range(n-3,-1,-1):
21            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]: 
22            
23                right[i] = right[i+1] +1
24            else:
25                right[i] = 2
26
27
28        for i in range(1,n-1):
29            mx = max(mx, left[i-1] +1, right[i+1] +1)
30
31            if( nums[i+1] - nums[i-1]) % 2 == 0 :
32                new = (nums[i+1] - nums[i-1]) //2
33                L = R = 1
34                
35                if i >= 2 and new == nums[i-1] - nums[i-2]:
36                    L = left[i-1]
37                if i <= n -3 and new == nums[i+2] - nums[i+1]: 
38                    R = right[i+1]
39                
40                mx = max(mx, R + L + 1)
41
42        
43        return max(mx, right[1] +1, left[-2] +1)
44        
45        
46        
47                
48            