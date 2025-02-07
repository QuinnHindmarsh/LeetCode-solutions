class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = max_sub = 0
        r = 1
        n = len(nums)

        if len(nums) < 2:
            return 1

        while r < n:
            if nums[r] <= nums[r-1]:
                max_sub = max(max_sub, (r - l))
                l = r 

            r += 1

        max_sub  = max(max_sub, (r-l))

        r = 1
        l = 0

        while r < n:
            if nums[r] >= nums[r-1]:
                max_sub = max(max_sub, (r - l))
                l = r 
            r += 1

        max_sub = max(max_sub, (r-l))

        return max_sub
