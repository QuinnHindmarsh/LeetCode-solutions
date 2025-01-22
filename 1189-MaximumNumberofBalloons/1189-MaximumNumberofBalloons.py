class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        freqs = {}
        cmin = 9999
        n = len(s)

        for i in range(n):
            if s[i] in "balon":
                freqs[s[i]] = freqs.get(s[i],0) + 1
            

        if len(freqs) < 5:
            return 0
        
        for key in freqs:
            if key in 'ban':
                cmin = min(cmin,freqs[key])
            else:
                cmin = min(cmin, freqs[key] // 2)


        return cmin
