# Last updated: 04/04/2026, 15:19:50
1class Solution:
2    def rearrangeArray(self, nums: List[int]) -> List[int]:
3        neggatives = []
4        possitives = []
5        ln = lp = 0
6
7        for num in nums:
8            if num >= 0: 
9                possitives.append(num)
10            else:
11                neggatives.append(num)
12
13        for i in range(0,len(nums),2): 
14            nums[i] = possitives[lp]
15            nums[i+1] = neggatives[ln]
16            lp += 1
17            ln += 1
18
19        return nums