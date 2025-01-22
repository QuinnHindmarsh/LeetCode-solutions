class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx != fx or sy != fy:
            return max(abs(sx-fx),abs(sy-fy)) <= t
        return t != 1