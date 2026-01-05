# Last updated: 05/01/2026, 15:13:03
1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        cur = [1]
4
5
6        for _ in range(1,rowIndex+1):
7            last = cur
8            cur = []
9
10            for i in range(len(last)+1):
11                if i == 0 or i == len(last):
12                    cur.append(1)
13                else:
14                    cur.append(last[i-1] + last[i])
15
16        return cur