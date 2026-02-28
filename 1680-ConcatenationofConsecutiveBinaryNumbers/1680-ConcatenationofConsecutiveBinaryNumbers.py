# Last updated: 28/02/2026, 20:48:18
1class Solution:
2    def concatenatedBinary(self, n: int) -> int:
3        bin_representation = []
4        for i in range(1,n+1):
5            bin_representation.append(bin(i)[2::])
6        return int(''.join(bin_representation),2) % 100_000_000_7 