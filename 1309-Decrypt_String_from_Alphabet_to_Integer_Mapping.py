""""
1309. Decrypt String from Alphabet to Integer Mapping
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

"""

# Solution one - looking ahead


class Solution(object):
    def freqAlphabets(self, s):

        txt = ''
        i = 0
        while i < (len(s)):
            if i+2 < len(s) and s[i+2] == '#':
                # Concatinates it as it is a string
                num = s[i] + s[i+1]
                i += 3
            else:
                num = s[i]
                i += 1
            # 97 is ASCII value for 'a'
            txt += chr(int(num)+96)
        return txt

# My solution
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/solutions/6210896/simple-looking-ahead-solution-by-quinnhi-23re/
