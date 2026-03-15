# Last updated: 15/03/2026, 12:26:58
1class Solution:
2    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
3        medians = []
4        tree = SortedList()
5        n = len(nums)
6
7        for i in range(k):
8            tree.add(nums[i])
9
10        for i in range(k,n+1):
11            if k % 2 == 1: 
12                medians.append(float(tree[k // 2]))
13            else:
14                median1 = tree[k // 2]
15                median2  = tree[(k // 2) -1]
16                medians.append(( median1 + median2) /2 )
17
18            if i < n: 
19                tree.add(nums[i])
20                tree.remove(nums[i-k])
21
22        return medians