# Last updated: 11/08/2025, 15:01:38
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums) -1, -1, -1):
            mn = float('inf')
            mn_idx = -1
            for j in range(i,len(nums)):
                if nums[j] > nums[i] and mn > nums[j]:
                    mn_idx = j
                    mn = nums[j]

            if mn != float('inf'):
                temp = nums[i]
                nums[i] = nums[mn_idx]
                nums[mn_idx] = temp
                nums[i+1::] = sorted(nums[i+1::])

                return

        nums.sort()
