class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        l, r = 0, n - 1
        maxL = h[l]
        maxR = h[r]
        ans = 0

        while l <= r:
            if maxL < maxR:
                ans += max(maxL - h[l],0)
                maxL = max(maxL, h[l])
                l += 1
            else:
                ans += max(maxR - h[r],0)
                maxR = max(maxR, h[r])
                r -= 1
        
        return ans