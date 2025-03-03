class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = defaultdict(int)
        mx = 0
        mn = float('inf')

        for i in range(len(s)):
            freqs[s[i]] += 1


        for key in freqs:
            n = freqs[key]
            if n % 2 == 1:
                mx = max(mx, n)
            else:
                mn = min(mn, n)
        
        return mx - mn
        