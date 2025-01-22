class Solution:
    def maxScore(self, s: str) -> int:
        rp = s[1::].count('1')
        lp = 1 if s[0] == '0' else 0
        maxScore = lp + rp

        for i in range(1,len(s)-1):
            rp -= 1 if s[i] == '1' else 0
            lp += 1 if s[i] == '0' else 0
            maxScore = max(maxScore,lp + rp)
        
        return maxScore