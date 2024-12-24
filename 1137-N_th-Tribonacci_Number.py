"""
1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/description/
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # Last
        last = 1
        # Second last
        Slast = 1
        # Third last
        Tlast = 0
        # We start at the 3rd tribonachi number, e.g. 0,1,1
        i = 3

        # base cases
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        while i <= n:
            if i == n:
                return last + Slast + Tlast
            else:
                # updates each value
                temp = last
                last += Slast + Tlast
                Tlast = Slast
                Slast = temp
                i += 1
# O(n) time and O(1) space
