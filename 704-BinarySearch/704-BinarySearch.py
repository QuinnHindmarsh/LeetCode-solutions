class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        i = bisect_left(nums,tar)
        
        # insertion point points to the number itself
        # and the insertion point isnt the end of the list
        if i != len(nums) and nums[i] == tar:
            return i
        else:
            return -1