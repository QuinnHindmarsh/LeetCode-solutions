class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp = 0
        rp = 0
        curSum = 0
        minValid = 0

        while rp < len(nums):
            curSum += nums[rp]

            if curSum >= target:
                while curSum - nums[lp] >= target:
                    curSum -= nums[lp]
                    lp +=1 

                if (rp-lp) + 1 < minValid or minValid == 0:
                    minValid = (rp-lp) + 1
            rp +=1 

        return minValid
