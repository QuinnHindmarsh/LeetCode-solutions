class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        Cmax = 0

        for rp in range(len(prices)):
            # New lowest price to buy on
            if prices[rp] < prices[lp]:
                lp = rp
            elif prices[rp] - prices[lp] > Cmax:
                #Current optimal solution
                Cmax = prices[rp] - prices[lp]
        
        return Cmax