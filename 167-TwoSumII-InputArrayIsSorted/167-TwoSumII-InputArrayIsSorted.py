# Last updated: 16/05/2025, 10:24:22
class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        l,r = 0, len(nums) -1
        while l < r:
            total = nums[l] + nums[r]

            if total > tar:
                r -=1
            elif total < tar:
                l += 1
            else:
                return [l+1,r+1]
        return []