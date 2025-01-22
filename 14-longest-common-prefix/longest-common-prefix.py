class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        while len(ans) < len(strs[0]):
            c = strs[0][len(ans)]
            for s in strs:
                if  (len(ans) >= len(s)) or s[len(ans)] != c:
                    return ans
            ans += c
        return ans
