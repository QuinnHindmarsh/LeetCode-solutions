class Solution:
    def numTrees(self, n):
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))