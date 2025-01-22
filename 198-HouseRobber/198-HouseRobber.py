class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = maxRob = 0

        # For each house it sees if you are best off robbing i-2 + the current one, or i-1
        for house in nums:
            temp = maxRob
            maxRob = max(maxRob, prev + house)
            prev = temp
        
        return maxRob

