# Last updated: 03/03/2026, 15:45:09
1class Solution:
2    def vowelConsonantScore(self, s: str) -> int:
3        v = c = 0 
4        for i in range(len(s)):
5            v += 1 if s[i] in ['a','e','i','o','u'] else 0      
6            c += 1 if s[i].isalpha() and s[i] not in ['a','e','i','o','u'] else 0
7
8        
9        return 0 if c == 0 else v//c