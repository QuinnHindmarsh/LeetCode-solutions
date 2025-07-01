# Last updated: 01/07/2025, 12:11:20
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        for i in range(32):
            if n & (1 << i):
                cnt += 1

        return cnt