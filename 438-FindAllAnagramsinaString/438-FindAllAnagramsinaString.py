class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        pchars = [0] * 26
        chars = [0] * 26
        l = r = 0


        if len(s) < len(p):
            return []

        for i in range(len(p)):
            pchars[ord(p[i])- 97] += 1

        while r < len(s):
            if (r - l) == len(p):
                chars[ord(s[l]) - 97] -=1
                l += 1
            chars[ord(s[r]) -97] +=1
            r += 1
            
        
            if chars == pchars:
                ans.append(l)

        return ans

        
