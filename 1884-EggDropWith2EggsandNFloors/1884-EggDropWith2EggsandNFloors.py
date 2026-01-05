# Last updated: 05/01/2026, 12:29:31
1class Solution:
2    def twoEggDrop(self, n: int) -> int:
3        m = 1 
4        while m * (m+1) /2 < n:
5            m +=1
6        return m