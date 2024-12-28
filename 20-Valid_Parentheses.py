"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        parren = {'(': ')', '{': '}', '[': ']'}

        for i in range(len(s)):
            # Add openning brackets to the stack
            if s[i] in parren:
                stack.append(s[i])
            else:
                # If it is a closing bracket, ensure that the last opening bracket matches this
                if len(stack) == 0:
                    return False
                l = stack.pop()
                # Checks that the equivilent closing bracket for the last opening one, matches the current closing
                if parren[l] != s[i]:
                    return False

        # Ensures there are no opening brackets without closing ones
        return len(stack) == 0

# My solution
# https://leetcode.com/problems/valid-parentheses/
