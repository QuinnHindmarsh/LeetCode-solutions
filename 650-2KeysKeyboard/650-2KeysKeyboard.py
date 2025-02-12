class Solution:
    def minSteps(self, n: int) -> int:
        x = 0
        p = 2
        while p**2 <= n:
            while n % p == 0:
                x += p
                n //= p
            p += 1

        return x + n if n > 1 else x