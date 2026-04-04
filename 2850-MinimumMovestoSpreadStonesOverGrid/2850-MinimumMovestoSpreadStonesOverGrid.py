# Last updated: 04/04/2026, 14:33:53
1class Solution:
2    def minimumMoves(self, grid: List[List[int]]) -> int:
3        extras = []
4        zeros = []
5
6        for i in range(3):
7            for j in range(3):
8                if grid[i][j] > 1:
9                    for _ in range(grid[i][j] - 1):
10                        extras.append((i, j))
11                elif grid[i][j] == 0:
12                    zeros.append((i, j))
13
14        def dfs(i, used):
15            if i == len(extras):
16                return 0
17
18            res = float('inf')
19            x1, y1 = extras[i]
20
21            for j in range(len(zeros)):
22                if not (used & (1 << j)):
23                    x2, y2 = zeros[j]
24                    cost = abs(x1 - x2) + abs(y1 - y2)
25                    res = min(res, cost + dfs(i + 1, used | (1 << j)))
26
27            return res
28
29        return dfs(0, 0)