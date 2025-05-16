# Last updated: 16/05/2025, 15:29:37
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lower_bound(nums, tar):
            l = 0 
            r = len(nums) -1 

            while l < r:
                mid = (l+r) // 2

                if nums[mid] > tar:
                    r = mid -1
                elif nums[mid] < tar:
                    l = mid +1
                else:
                    r = mid

            return l if nums[l] == target else -1

        def upper_bound(nums,tar):
            l = 0
            r = len(nums) -1

            while l < r: 
                mid = (l + r+1) // 2

                if nums[mid] > tar:
                    r = mid -1 
                elif nums[mid] < target:
                    l = mid +1
                else:
                    l = mid

            return r if nums[r] == target else -1

        if not nums:
            return [-1,-1]

        return [lower_bound(nums, target), upper_bound(nums, target)]
