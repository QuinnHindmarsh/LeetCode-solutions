# Last updated: 27/06/2025, 16:02:04
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        memo = {}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i >= len(s1) or j >= len(s2):
                return 0 

            mx = 0

            if s1[i] == s2[j]: 
                mx = dfs(i+1,j+1) + 1
            else:
                mx = max(mx, dfs(i+1,j), dfs(i,j+1))

            memo[(i,j)] = mx
            return memo[(i,j)]

            

        return dfs(0,0)
