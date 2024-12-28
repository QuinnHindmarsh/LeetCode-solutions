"""
191. Number of 1 Bits
Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight).


"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Converts to binary and removes the first 2 chars '0b'
        c = bin(n)[2:]
        ans = 0

        for i in range(len(c)):
            # Adds the value of the binary to the current count
            ans += int(c[i])

        return ans


# My solution
# https://leetcode.com/problems/number-of-1-bits/solutions/6195585/simple-olog-n-solution-by-quinnhindmarsh-mvd8/
