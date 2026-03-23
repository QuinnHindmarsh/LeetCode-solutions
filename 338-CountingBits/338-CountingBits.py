# Last updated: 23/03/2026, 21:21:22
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        return [bin(i).count('1') for i in range(n+1)]