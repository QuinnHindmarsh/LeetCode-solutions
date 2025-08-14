# Last updated: 14/08/2025, 13:14:26
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for sorted_i in range(len(nums)):
            mn = float('inf')
            mn_idx = -1
            for j in range(sorted_i, len(nums)):
                if nums[j] < mn:
                    mn = nums[j]
                    mn_idx = j

            temp = nums[sorted_i] 
            nums[sorted_i] = nums[mn_idx]
            nums[mn_idx] = temp

        
