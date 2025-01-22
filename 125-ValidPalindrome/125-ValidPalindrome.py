# Solution one O(n) time, O(n) space - 3 O(n) itterations
class Solution(object):
    def isPalindrome(self, s):
        stripped_s = ''.join(char.lower() for char in s if char.isalnum())
        return stripped_s == stripped_s[::-1]