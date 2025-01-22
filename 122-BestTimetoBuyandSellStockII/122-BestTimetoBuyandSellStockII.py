class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            i = 0
            Profit = 0
            holdStock = False

            while i < len(prices):
                if i == len(prices) -1:
                    if holdStock:
                        Profit += prices[i]
                else:
                    if prices[i] < prices[i+1] and not holdStock:
                        holdStock = True
                        Profit -= prices[i]
                    elif prices[i] >prices[i+1] and holdStock:
                        Profit += prices[i]
                        holdStock = False
                i += 1 
            return Profit 
