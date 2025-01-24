class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spaceIdx = -1
        charIdx = None
        n = len(s)

        for i in range(n-1, -2, -1):
            if charIdx == None:
                if s[i] != ' ':
                    charIdx = i 
            elif i == -1 or s[i] == ' ':
                spaceIdx = i
                break
        
        if charIdx == None:
            return 0
        return (charIdx - spaceIdx)
