class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        mapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        i = 0

        while i < len(s):
            if i +1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
                ans += mapping[s[i+1]]
                ans -= mapping[s[i]]
                i += 1
            else:
                ans += mapping[s[i]]
            i += 1

        return ans 
