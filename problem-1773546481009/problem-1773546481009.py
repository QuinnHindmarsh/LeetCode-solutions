# Last updated: 15/03/2026, 14:18:01
1class Solution:
2    def countCommas(self, n: int) -> int:
3        cnt = 1000
4        commmas = 0
5
6        while cnt <= n: 
7            commmas += n - cnt +1
8            cnt *= 1000
9
10        return commmas