class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if k * m > n:
            return -1

        def verify(day):
            lp = rp = 0
            cnt = 0

            while rp < n:
                if bloomDay[rp] - day > 0:
                    lp = rp +1
                
                if (rp-lp) + 1 == k:
                    cnt += 1
                    lp = rp +1
                rp += 1

            return cnt >= m

        def bin_search():
            l = 0
            r = max(bloomDay)

            while l < r:
                mid = l + ((r-l) // 2)

                if verify(mid):
                    r = mid
                else:
                    l = mid + 1
            
            return l

        return bin_search()