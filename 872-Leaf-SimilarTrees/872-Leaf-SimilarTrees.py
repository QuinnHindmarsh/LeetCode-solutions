# Last updated: 20/06/2026, 17:48:16
1class Solution:
2    def lenLongestFibSubseq(self, arr: List[int]) -> int:
3        # if it ends at arr[i] then we have combinations of previous elements 
4
5        num_set = set(arr)
6        memo = {}
7        mx = 0
8        arr.sort()
9
10        def dp(current, previous):
11            if (current,previous) in memo: 
12                return memo[(current,previous)]
13            k = current - previous
14
15            if k < previous and k in num_set: 
16                memo[(current,previous)] = dp(previous, k) + 1 
17                return memo[(current,previous)]
18
19            return 0
20
21        for i in range(len(arr)):
22            for j in range(i):
23                mx = max(mx, dp(arr[i],arr[j]))
24
25        return mx + 2 if mx != 0 else mx