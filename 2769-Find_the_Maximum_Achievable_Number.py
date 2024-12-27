"""
2769. Find the Maximum Achievable Number
https://leetcode.com/problems/find-the-maximum-achievable-number/description/
Given two integers, num and t. A number is achievable if it can become equal to num after applying the following operation:

Increase or decrease the number by 1, and simultaneously increase or decrease num by 1.
Return the maximum achievable number after applying the operation at most t times.
"""


# Soluition one - simple maths O(1) time and space
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # For each value of t you can bring the max achivable number 2 closer
        # Increase num by 1, decrease max achivable by 1
        return num + (2 * t)


# Solution two - simulation O(t) time and O(1) space
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        maxAch = 0

        for i in range(t):
            # Num is increased by 1 each time
            # Max achievable is decreased by one each time
            maxAch -= 1
            num += 1

        return num - maxAch

# Solution three - recursive O(t) time and O(t) space


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        def find_max(num, t):
            if t == 0:
                return num
            return find_max(num+2, t-1)

        return find_max(num, t)


# Solution four - bit manipulation
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # Same as * 2
        return num + (t << 1)

# My solution
# https: //leetcode.com/problems/find-the-maximum-achievable-number/solutions/6191170/4-solutions-recursion-iteration-bit-mani-m5lm/
