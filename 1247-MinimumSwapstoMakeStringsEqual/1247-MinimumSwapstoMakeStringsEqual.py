class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        unevenPairs = defaultdict(int)
        freqs = defaultdict(int)
        cnt = 0

        for i in range(len(s1)):
            freqs[s1[i]] += 1
            freqs[s2[i]] += 1
            if s1[i] != s2[i]:
                unevenPairs[(s1[i], s2[i])] += 1
        
        for l in freqs:
            if freqs[l] % 2 == 1:
                return -1

        for pair in unevenPairs:
            cnt += (unevenPairs[pair] +1) //2
        
        return cnt