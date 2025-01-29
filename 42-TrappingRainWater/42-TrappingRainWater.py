class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        maxl = 0
        maxr = 0
        lh = []
        arr = [0] * n
        ans = 0
        

        for i in range(0,n):
            lh.append(maxl)
            maxl = max(maxl, h[i])

        for i in range(n-1,-1,-1):
            arr[i] = min(lh[i],maxr)
            maxr = max(maxr, h[i])

        for i in range(n):
            ans += max(arr[i] - h[i], 0)
        
        return ans