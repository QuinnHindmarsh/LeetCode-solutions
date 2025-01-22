class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        lp = 0
        rp = len(height) -1

        while lp < rp:
            l = height[lp]
            r = height[rp]
            max_water = max(max_water, min(l,r) * (rp-lp))
        
            if l < r:
                lp +=1
            elif r < l:
                rp -=1
            else:
                lp +=1
                rp -=1
        return max_water