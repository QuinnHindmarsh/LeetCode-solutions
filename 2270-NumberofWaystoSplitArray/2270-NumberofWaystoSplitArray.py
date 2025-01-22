class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i-1]

        for i in range(0,n-1):
            if nums[i] >= nums[-1] - nums[i]:
                ans +=1

        return ans