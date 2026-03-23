# Last updated: 23/03/2026, 21:20:30
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = []
4
5
6        for i in range(n+1): 
7            ans.append(bin(i).count('1'))
8
9        return ans