# Last updated: 27/06/2026, 16:03:25
1class Solution:
2    def totalHammingDistance(self, nums: List[int]) -> int:
3        count = [0] * len(bin(max(nums))[2::])
4        ans = 0 
5
6        for num in nums:
7            b_num = bin(num)[2::]
8            b_num = b_num[::-1]
9            for i in range(len(b_num)):
10                if b_num[i] == '1': 
11                    count[i] += 1
12
13        for i in range(len(count)): 
14            with_ = count[i]
15            without = len(nums) - with_
16            ans += with_ * without
17
18        return ans