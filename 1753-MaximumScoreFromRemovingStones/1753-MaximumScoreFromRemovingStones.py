# Last updated: 11/03/2026, 15:27:47
1class Solution:
2    def maximumScore(self, a: int, b: int, c: int) -> int:
3        a,b,c = sorted([a,b,c])
4        points = a 
5
6        for _ in range(a): 
7            if c > b: 
8                c-= 1
9            else: 
10                b -=1
11
12        points += b
13        return points
14