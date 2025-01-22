class Solution:
    def checkRecord(self, s: str) -> bool:
        aUsed = False

        for i in range(len(s)):
            if s[i] == 'A':
                if aUsed:
                    return False
                aUsed = True
            if i-2 >= 0 and s[i] == 'L':
                if s[i-2:i+1] == 'LLL':
                    return False
        return True
