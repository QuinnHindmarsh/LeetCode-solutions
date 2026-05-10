# Last updated: 10/05/2026, 12:01:34
1class Solution:
2    def concatWithReverse(self, nums: list[int]) -> list[int]:
3        return nums + nums[::-1]