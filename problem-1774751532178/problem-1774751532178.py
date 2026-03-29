# Last updated: 29/03/2026, 13:02:12
1class Solution:
2    def firstMatchingIndex(self, s: str) -> int:
3        n = len(s)
4
5        for i in range((len(s)+1)//2): 
6            if s[i] == s[n - i - 1]:
7                return i
8        return -1