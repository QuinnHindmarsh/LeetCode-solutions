class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        
        for i in range(len(s)):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
        
        ans ^= ord(t[-1])

        return chr(ans)