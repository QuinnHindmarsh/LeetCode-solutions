"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


# Solution one O(n) time, O(n) space - 3 O(n) itterations
class Solution(object):
    def isPalindrome(self, s):
        stripped_s = ''.join(char.lower() for char in s if char.isalnum())
        return stripped_s == stripped_s[::-1]

# Solution two O(n) time, O(1) space - one O(n) itteration


class Solution(object):
    def isPalindrome(self, s):
        lp = 0
        rp = len(s)-1

        while lp < rp:
            # ensures both left and right pointer are letters
            while lp < rp and not s[lp].isalnum():
                lp += 1

            while lp < rp and not s[rp].isalnum():
                rp -= 1

            if s[rp].lower() != s[lp].lower():
                return False

            lp += 1
            rp -= 1

        return True

# My solution
# https://leetcode.com/problems/valid-palindrome/solutions/6183714/two-solutions-strip-reverse-string-and-t-mv70/
