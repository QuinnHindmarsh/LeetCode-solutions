# Last updated: 01/07/2025, 15:40:06
class Solution:
    def reverse(self, n: int) -> int:
        ans = 0
        sign = 1 

        if n < 0:
            sign = -1
            n *= -1

        while n > 0:
            next_digit = n % 10
            n //= 10

            if ans >= ((2**31 -1) // 10) + next_digit:
                return 0

            ans = (ans * 10) + next_digit

        return ans * sign