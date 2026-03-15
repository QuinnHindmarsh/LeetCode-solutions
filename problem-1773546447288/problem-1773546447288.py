# Last updated: 15/03/2026, 14:17:27
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
11
12
13# 1000
14# 1001
15# 1002
16# 1003
17# 1004
18# 1005
19# 1006
20# 1007
21# 1008
22# 1009
23# 1010
24
25