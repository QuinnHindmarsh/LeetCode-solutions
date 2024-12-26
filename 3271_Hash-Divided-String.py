"""
# 3271. Hash Divided String
# https://leetcode.com/problems/hash-divided-string/description/

You are given a string s of length n and an integer k, where n is a multiple of k. Your task is to hash the string s into a new string called result, which has a length of n / k.

First, divide s into n / k 
substrings
, each with a length of k. Then, initialize result as an empty string.

For each substring in order from the beginning:

The hash value of a character is the index of that character in the English alphabet (e.g., 'a' → 0, 'b' → 1, ..., 'z' → 25).
Calculate the sum of all the hash values of the characters in the substring.
Find the remainder of this sum when divided by 26, which is called hashedChar.
Identify the character in the English lowercase alphabet that corresponds to hashedChar.
Append that character to the end of result.
Return result.
"""


# solution one unoptimised- O(n) time O(1) space
# very consistantly at 19ms runtime and beats 41%
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = ""
        i = 0

        while i+k <= len(s):
            subsetSum = 0
            for j in range(i, i+k):
                subsetSum += ord(s[j]) - ord('a')
            remainder = subsetSum % 26
            # Adds the char this segment responds to onto the string
            ans += chr(ord('a') + remainder)

            i += k
        return ans


# solution one optimised- O(n) time O(1) space
# very consistantly at 11ms runtime and beats 90%
# with only very small constant time changes
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = ""
        i = 0
        slen = len(s)

        while i+k <= slen:
            subStr = 0
            for j in range(i, i+k):
                # 97 is acii value for 'a'
                subStr += ord(s[j]) - 97
            remainder = subStr % 26
            # Adds the char this segment responds to onto the string
            ans += chr(97 + remainder)

            i += k
        return ans

# My solution
# https://leetcode.com/problems/hash-divided-string/solutions/6187599/python-ascii-nested-loop-simulation-by-q-17qo/
