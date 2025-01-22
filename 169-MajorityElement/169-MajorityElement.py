class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        me = nums[0]

        for e in nums:
            if count <= 0:
                me = e

            if e == me:
                count +=1
            else:
                count -=1
        return me