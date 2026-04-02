# Last updated: 02/04/2026, 12:31:12
1class Solution:
2    def stoneGameIX(self, stones: List[int]) -> bool:
3        freq = defaultdict(int)
4        for x in stones: freq[x % 3] += 1
5        
6        if freq[0]%2 == 0: return bool(freq[1] and freq[2])
7        return abs(freq[1] - freq[2]) >= 3