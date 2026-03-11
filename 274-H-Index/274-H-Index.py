# Last updated: 11/03/2026, 14:31:27
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        citations.sort()
4        n = len(citations)
5
6        for i in range(n):
7            if citations[i] >= n - i:
8                return n - i
9
10        return 0