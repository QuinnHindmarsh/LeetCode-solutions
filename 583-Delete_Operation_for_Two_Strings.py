"""
583. Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        # Initalises current min costs
        for i in range(n+1):
            dp[0][i] = i

        for j in range(m+1):
            dp[j][0] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                # If the letters equal we dont neeed to change anything
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # We see if we are best off deleting the char from word 1 or word 2
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        for j in range(len(dp)):
            print(dp[j])
        return dp[-1][-1]

# My solution
# https://leetcode.com/problems/delete-operation-for-two-strings/solutions/6211237/dp-bottom-up-tabulation-by-quinnhindmars-uyw8/
