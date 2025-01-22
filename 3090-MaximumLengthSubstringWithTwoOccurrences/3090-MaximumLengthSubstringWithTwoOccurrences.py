class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        occur = {}
        maxSubstring = 0
        n = len(s)
        lp = 0
        rp = 0
        
        while rp < n:
            occur[s[rp]] = occur.get(s[rp],0) +1

            while occur[s[rp]] > 2:
                occur[s[lp]] -=1 
                lp +=1

            maxSubstring = max(maxSubstring, (rp-lp) +1)
            rp +=1
            
    

        return maxSubstring
