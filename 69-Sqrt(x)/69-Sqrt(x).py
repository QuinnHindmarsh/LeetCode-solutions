class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        if x == 2: return 1
        
        while l < r:
            mid = l + (r-l) //2

            if mid**2 < x:
                l = mid +1
            elif mid**2 > x:
                r = mid
                mid -= 1
                if mid**2 < x:
                    return mid
            else:
                return mid
        return l

        2 
        1
