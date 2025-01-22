class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        maxDist = nums[0]
        i = 0
        while i <= maxDist and maxDist < len(nums)-1:
            maxDist = max(maxDist,i+nums[i])
            i+=1

        if maxDist < len(nums)-1:
            return False
        return True

