"""
9. Palindrome Number
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

# Solution one - simple reverse O(n) time and space where n is the amount of digits in x


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if the reversed version == the non reversed version
        return str(x) == str(x)[::-1]

# Solution two - 2 pointers O(n) time and space where n is the amount of digits in x


class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        lp, rp = 0, len(numStr) - 1

        while lp < rp:
            if numStr[lp] != numStr[rp]:
                return False
            lp += 1
            rp -= 1

        return True

# My solution
# https://leetcode.com/problems/palindrome-number/solutions/6196128/one-line-solution-two-pointers-by-quinnh-5joa/
