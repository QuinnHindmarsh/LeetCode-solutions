"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        Cmax = 0

        for rp in range(len(prices)):
            # New lowest price to buy on
            if prices[rp] < prices[lp]:
                lp = rp
            elif prices[rp] - prices[lp] > Cmax:
                # Current optimal solution
                Cmax = prices[rp] - prices[lp]

        return Cmax

# My solution
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/6179828/two-pointer-method-by-quinnhindmarsh-jkmo/

# O(n) time complexity, O(1) space complexity
