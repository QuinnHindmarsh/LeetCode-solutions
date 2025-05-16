# Last updated: 16/05/2025, 14:39:05
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        l = r = 0
        max_len = highest_freq = 0

        while r < len(s):
            freqs[s[r]] += 1
            highest_freq = max(highest_freq, freqs[s[r]])

            if (r-l+1) - highest_freq > k:
                freqs[s[l]] -=1 
                l += 1

            max_len = r-l+1
            r +=1

        return max_len