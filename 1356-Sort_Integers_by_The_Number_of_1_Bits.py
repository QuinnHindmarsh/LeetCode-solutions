"""
1356. Sort Integers by The Number of 1 Bits
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

"""

# O(n) time O(n) space


class Solution(object):
    def sortByBits(self, arr):
        # Converts each number to binary, counts the amount of 1's uses that as the main key, then when there are ties compares the Key itself
        return sorted(arr, key=lambda n: (bin(n).count('1'), n))

# My soltuion
# https: //leetcode.com/problems/sort-integers-by-the-number-of-1-bits/solutions/6207962/clean-1-line-with-explanation-by-quinnhi-90t6/
