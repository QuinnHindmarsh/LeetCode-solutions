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

        def bin_search(l,h):
            if not l < h:
                return l
            mid = (l+h) // 2

            if verify(mid):
                h = mid
            else:
                l = mid + 1
            return bin_search(l,h)

        return bin_search(min(bloomDay),max(bloomDay))