class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache
        def find_nth(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            else:
                return find_nth(n - 1) + find_nth(n -2 ) + find_nth(n-3)
        return find_nth(n)