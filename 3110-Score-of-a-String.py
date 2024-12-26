class Solution(object):
    def scoreOfString(self, s):
        i = 0
        # Score sum
        sSum = 0
        # Less then len(s) - 1 as we want to stop at second last index
        while i < (len(s) - 1):
            # Adds absolute difference
            sSum += abs(ord(s[i]) - ord(s[i+1]))
            i += 1
        return sSum
