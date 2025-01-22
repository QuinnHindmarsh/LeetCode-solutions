class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        last = 1
        cur = 2
        i = 2

        while i < n:
            temp = cur
            cur += last
            last = temp
            i += 1

        return cur
