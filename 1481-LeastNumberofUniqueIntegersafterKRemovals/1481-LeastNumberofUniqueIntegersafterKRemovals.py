# Last updated: 11/03/2026, 15:33:06
1class Solution:
2    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
3        freq = Counter(arr)
4        removed = 0 
5        qty = sorted(freq.values())
6
7        for cnt in qty: 
8            k -= cnt
9            if k < 0:
10                break
11            removed += 1
12        
13        return len(freq) - removed