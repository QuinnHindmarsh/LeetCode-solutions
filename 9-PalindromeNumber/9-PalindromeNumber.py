class Solution:
    def isPalindrome(self, x: int) -> bool:
        #check if the reversed version == the non reversed version
        return str(x) == str(x)[::-1]