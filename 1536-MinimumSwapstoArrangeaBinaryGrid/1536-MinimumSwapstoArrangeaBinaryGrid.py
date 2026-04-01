# Last updated: 01/04/2026, 18:36:48
1class Solution:
2    def minSwaps(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4
5        arr_representation = [0] * n 
6        ans = 0
7
8        for r in range(n):
9            for c in range(n - 1, -1, -1):
10                if grid[r][c] == 1:
11                    break
12                arr_representation[r] += 1
13
14        for i in range(n): 
15            for j in range(i,n):
16                if arr_representation[j] >= n - i - 1:
17                    ans += j - i 
18                    val = arr_representation[j]
19                    for k in range(j, i, -1):
20                        arr_representation[k] = arr_representation[k - 1]
21                    break 
22                if j == n-1: 
23                    return -1
24
25        return ans
26        
27                    