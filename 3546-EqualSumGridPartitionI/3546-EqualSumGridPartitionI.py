# Last updated: 05/01/2026, 14:11:38
1class Solution:
2    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
3        row_sum = []
4        col_sum = []
5        n = len(grid)
6        m = len(grid[0])
7
8        for i in range(n):
9            cnt = 0 
10            for j in range(m):
11                cnt += grid[i][j]
12
13            row_sum.append(cnt)
14
15        for i in range(m):
16            cnt = 0 
17            for j in range(n):
18                cnt += grid[j][i]
19            col_sum.append(cnt)
20
21        row_total = sum(row_sum)
22        cnt = 0 
23        for i in range(n-1):
24            cnt += row_sum[i]
25            if cnt * 2 == row_total:
26                return True
27
28        col_total = sum(col_sum)
29        cnt = 0 
30        for i in range(m-1):
31            cnt += col_sum[i]
32            if cnt * 2 == col_total:
33                return True
34        return False