class Solution:
    def numberOfMatches(self, n: int,matches=0) -> int:
        if n == 1: return matches
        if n % 2 == 0: return self.numberOfMatches(n//2, matches + n //2)
        else: return self.numberOfMatches(n//2 +1, matches + n//2)