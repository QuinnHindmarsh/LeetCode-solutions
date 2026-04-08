# Last updated: 08/04/2026, 16:42:39
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        uppercase = {} 
4        lowercase = defaultdict()
5        cnt = 0 
6
7
8        for idx, c in enumerate(word): 
9            if c.isupper() and c.lower() not in uppercase: 
10                uppercase[c.lower()] = idx
11
12            else:
13                lowercase[c] = idx
14
15
16        for c, idx in lowercase.items(): 
17            if c in uppercase and idx < uppercase[c]: 
18                cnt += 1 
19        
20        return cnt
21
22             