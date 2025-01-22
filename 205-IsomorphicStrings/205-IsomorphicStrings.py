class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMapping = {}
        tMapping = {}

        for i in range(len(s)):
            if s[i] in sMapping:
                if sMapping[s[i]] != t[i]:
                    return False
            elif t[i] in tMapping:
                return False
            else:
                sMapping[s[i]] = t[i]
                tMapping[t[i]] = s[i]
        return True
