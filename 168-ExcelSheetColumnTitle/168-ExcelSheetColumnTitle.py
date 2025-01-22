class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        i = 26
        
        while n > 0:
            n -=1
            ans += chr(65 + n % 26)
            n //= 26


        return ans[::-1]