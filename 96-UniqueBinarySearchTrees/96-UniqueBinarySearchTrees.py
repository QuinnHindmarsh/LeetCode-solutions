class Solution:
    def numTrees(self, n):
        return math.comb(2*n,n) // (n+1)