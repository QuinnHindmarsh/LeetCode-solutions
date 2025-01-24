class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = defaultdict(int)
        ans = 0
        odd = False
        for c in s:
            freqs[c] += 1
        
        for key in freqs:
            if freqs[key] % 2 == 1:
                odd = True
                freqs[key] -=1
            ans += freqs[key]

        return ans + 1 if odd else ans 