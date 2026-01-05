# Last updated: 05/01/2026, 15:26:48
1class Solution:
2    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
3
4        r = len(matrix)
5        c = len(matrix[0])
6        r_min = [float('inf')] * r
7        c_max = [-float('inf')] * c
8        ans = []
9        
10        for i in range(c):
11            for j in range(r):
12                r_min[j] = min(r_min[j], matrix[j][i])
13                c_max[i] = max(c_max[i], matrix[j][i])
14        
15
16        for i in range(c):
17            for j in range(r):
18                if matrix[j][i] == c_max[i] == r_min[j]:
19                    ans.append(matrix[j][i])
20
21        return ans