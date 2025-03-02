class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l, r = 0,1
        mx = 1
        if len(nums) == 1:
            return 1 

        while r < len(nums):
            if nums[r] <= nums[r-1]:
                l = r
            r += 1
            mx = max(mx, (r-l))

        return mx
        