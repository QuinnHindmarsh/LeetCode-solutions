class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLen = len(needle)

        if nLen > len(haystack):
            return -1


        for i in range((len(haystack) - nLen)+1):
            print(i)
            if haystack[i:i+nLen] == needle:
                return i

        return -1 