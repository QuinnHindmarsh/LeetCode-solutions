class Solution:
    def checkOverlap(self, radius: int, cx: int, cy: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearX = max(x1, min(cx, x2))
        nearY = max(y1, min(cy,y2))
        dist = (nearY - cy) **2 + (nearX - cx) ** 2

        return dist <= radius* radius