class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # try all possible combinations
        min_mountain_sum = float('inf') 
        for i in range(len(nums) -2):
            for j in range(i+1, len(nums) -1):
                for k in range(j +1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        min_mountain_sum = min(min_mountain_sum, nums[i] + nums[j] + nums[k])
        
        if min_mountain_sum < float('inf'):
            return min_mountain_sum
        return -1
