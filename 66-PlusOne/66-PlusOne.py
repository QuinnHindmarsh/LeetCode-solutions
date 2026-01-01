# Last updated: 01/01/2026, 10:21:09
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        
4        for i in range(len(digits)-1,-1,-1):
5            if digits[i] == 9:
6                digits[i] = 0
7            else:
8                digits[i] += 1
9                return digits
10
11        return [1] + digits
12                