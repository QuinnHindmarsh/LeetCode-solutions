# Last updated: 08/04/2026, 16:13:41
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
3        reserved = {}
4        for r, s in reservedSeats:
5            if 2 <= s <= 9:
6                reserved.setdefault(r, set()).add(s)
7        
8        res = 2 * n  
9
10
11        for r, seats in reserved.items():
12            left = all(s not in seats for s in [2,3,4,5])
13            right = all(s not in seats for s in [6,7,8,9])
14            mid = all(s not in seats for s in [4,5,6,7])
15            
16            if left and right:
17                pass
18            elif left or right or mid:
19                res -= 1
20            else:
21                res -= 2
22        
23        return res