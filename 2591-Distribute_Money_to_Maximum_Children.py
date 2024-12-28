"""
2591. Distribute Money to Maximum Children
https://leetcode.com/problems/distribute-money-to-maximum-children/description/

You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.
"""


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Not possible to distribute money
        if children > money:
            return -1
        # Gives each children $1
        money -= children

        # The min of this is the max that could have 8
        ans = min(money // 7, children)
        money -= ans * 7

        # If there is still money and children left, one child will need
        # to be given more money, thus not have exactly 8
        if ans - children == 0 and money != 0:
            return ans - 1
        # If there is exactly one child and exactly 3 left, that money will
        # need to be split across 2 children as no child can have $4
        if children - ans == 1 and money == 3:
            return ans - 1
        return ans

# My solution
# https://leetcode.com/problems/distribute-money-to-maximum-children/solutions/6187787/math-solution-with-basic-break-down-of-t-urgz/
