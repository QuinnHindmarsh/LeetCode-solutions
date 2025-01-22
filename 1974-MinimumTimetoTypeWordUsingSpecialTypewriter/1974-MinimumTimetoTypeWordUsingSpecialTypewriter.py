class Solution:
    def minTimeToType(self, s: str) -> int:
        cur = 'a'
        ans = 0

        for i in range(len(s)):
            val = abs(ord(cur) - ord(s[i]))

            ans += min(val, abs(val-26)) +1
            cur = s[i]

        return ans 