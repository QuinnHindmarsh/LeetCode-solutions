
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        n = len(piles) // 3
        piles.sort(reverse=True)

        i = 0
        while i < 2*n:
            coins += piles[i+1]
            i+=2
        
        return coins
