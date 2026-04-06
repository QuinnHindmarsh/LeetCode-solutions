# Last updated: 06/04/2026, 15:57:39
1class Solution:
2    def increasingTriplet(self, nums: List[int]) -> bool:
3        mn1 = mn2 = float('inf')
4
5        for num in nums: 
6            if num > mn2: 
7                return True
8
9            if num < mn2 and num > mn1: 
10                mn2 = num 
11            elif num <mn1: 
12                mn1 = num 
13        return False