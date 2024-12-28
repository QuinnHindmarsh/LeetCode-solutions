"""
https://leetcode.com/problems/construct-the-longest-new-string/description/
You are given three integers x, y, and z.

You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB". You want to choose some (possibly all or none) of these strings and concatenate them in some order to form a new string. This new string must not contain "AAA" or "BBB" as a substring.

Return the maximum possible length of the new string.

A substring is a contiguous non-empty sequence of characters within a string.
"""


# Solution one - back tracking - TLE
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # no y after z
        # no z after x
        # no x after x
        # no y after y
        self.maxLen = 0

        self.backtrack(0, x, y, z, None)
        return self.maxLen

    def candaite(self, x, y, z, lastUsed):
        can = []
        if x > 0 and lastUsed != 'x':
            can.append('x')
        if z > 0 and (lastUsed != 'x'):
            can.append('z')
        if y > 0 and (lastUsed != 'z' and lastUsed != 'y'):
            can.append('y')

        return can

    def backtrack(self, cLen, x, y, z, lastUsed):
        can = self.candaite(x, y, z, lastUsed)
        self.maxLen = max(cLen, self.maxLen)

        for c in can:
            if c == 'x':
                self.backtrack(cLen+2, x-1, y, z, 'x')
            elif c == 'y':
                self.backtrack(cLen+2, x, y-1, z, 'y')
            elif c == 'z':
                self.backtrack(cLen+2, x, y, z-1, 'z')

# Solution two - O(1) time and space


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # x - aa
        # y - bb
        # z - ab
        # no z after x
        # no x after x
        # no y after z
        # no y after z

        # You can always use up all z as you can continously do zzz, so we add 2z to our final length
        # We can also repeat yz as many times as min(y,z)
        # If y != z we can increase this by 2 as an addional one of these can be added. e.g. either yxyz or xyzx
        if y == x:
            return (4 * x) + (2 * z)
        else:
            return (4 * min(y, x)) + 2 + (2 * z)

# My solution
# https://leetcode.com/problems/construct-the-longest-new-string/solutions/6195870/maths-with-explanation/
