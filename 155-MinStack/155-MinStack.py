# Last updated: 21/08/2025, 16:59:13
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        ans = 0
        cur_max = 0 

        for coin in coins: 
            if cur_max >= target:
                return ans

            if coin <= cur_max +1:
                cur_max += coin
            else:
                while cur_max + 1 < coin  and cur_max < target:
                    ans += 1
                    cur_max *= 2
                    cur_max += 1
                cur_max += coin

        while cur_max < target:
            ans += 1
            cur_max *= 2
            cur_max += 1

        return ans