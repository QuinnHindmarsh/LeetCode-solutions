# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
"""


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Keeps track of the coins we have
        coins = 0
        # The pile of coins will always be 3n
        n = len(piles) // 3
        # Sorts in descending  order
        piles.sort(reverse=True)

        # Itterates n times, we get the second largest remaining
        # coin each itteration
        i = 0
        while i < 2*n:
            coins += piles[i+1]
            i += 2

        return coins


# My solution link
# https: //leetcode.com/problems/maximum-number-of-coins-you-can-get/solutions/6179294/greedy-solution-beats-95-by-quinnhindmar-fatg/

"""
Complexity 
Time complexity:
O(n) - As we do a linear amount of work for each n itterations

Space complexity:
O(n) - We modify the given input, in python the standard library
sorting method is also not in-place
"""
