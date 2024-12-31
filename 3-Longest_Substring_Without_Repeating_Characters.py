"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.
"""

# Solution one - sliding window with set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keeps track of all letters in the current sub string
        seen = set()
        lp = 0
        ans = 0

        for rp in range(len(s)):
            # When the value has already be seen we increment the left pointer until it is no longer in the substring
            while s[rp] in seen:
                seen.remove(s[lp])
                lp += 1
            # adds current element to set
            seen.add(s[rp])
            # Updates ans
            ans = max(ans, (rp-lp)+1)

        return ans

# Solution two - two pointer with hashmap and set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        lp = 0
        ans = 0

        for rp in range(len(s)):
            if s[rp] in seen:
                # Sets the left pointer to 1 index past the last occurance
                # If the last occurace is in the current scope i.e. > lp
                lp = seen[s[rp]][-1] + 1 if seen[s[rp]][-1] + 1 > lp else lp

            if s[rp] in seen:
                seen[s[rp]].append(rp)
            else:
                seen[s[rp]] = [rp]

            ans = max(ans, (rp-lp)+1)

        return ans
