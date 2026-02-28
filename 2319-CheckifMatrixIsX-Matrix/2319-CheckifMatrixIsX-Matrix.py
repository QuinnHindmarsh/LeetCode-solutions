# Last updated: 28/02/2026, 20:42:30
1class Solution:
2    def checkXMatrix(self, grid: List[List[int]]) -> bool:
3
4                
5
6        for i in range(len(grid)):
7            for j in range(len(grid[0])):
8                if i == j or i +j == len(grid)-1: 
9                    if grid[i][j] == 0:
10                        return False
11                else:
12                    if grid[i][j] != 0:
13                        return False
14        return True
15
16# [0,0,0,0,1],
17# [0,4,0,1,0],
18# [0,0,5,0,0],
19# [0,5,0,2,0],
20# [4,0,0,0,2]