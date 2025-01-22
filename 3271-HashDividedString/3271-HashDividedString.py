class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = []
        newLen = len(s) // k

        for i in range(newLen):
            hashVal = 0
            for j in range(i*k, i*k+k,1):
                hashVal += ord(s[j]) - 97
            ans.append(chr(hashVal % 26 + 97))
        
        return "".join(ans)
